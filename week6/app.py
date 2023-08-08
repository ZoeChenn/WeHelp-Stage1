import os
import mysql.connector
from flask import Flask
from flask import request
from flask import redirect, url_for
from flask import render_template
from flask import session
from dotenv import load_dotenv

# 加載環境變數配置文件
load_dotenv()

# 使用 os.getenv() 讀取環境變數
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")

# 建立 Application 物件
app = Flask( 
  __name__, # 靜態檔案的資料夾名稱
  static_folder = 'static',
  static_url_path = '/',
  template_folder = 'templates',
) # 所有在 static 資料夾底下的檔案，都對應到網址路徑 /static/檔案名稱

# 設定 Session 密鑰
app.secret_key = SECRET_KEY

# 連線到資料庫
con = mysql.connector.connect(
  user = DB_USER,
  password = DB_PASSWORD,
  host = DB_HOST,
  database = DB_NAME
)
print("資料庫連線成功")

# 建立 Cursor 物件，用來對資料庫下 SQL 指令
cursor = con.cursor()

# 檢查帳號是否重複
def check_account(account):
  cursor.execute("SELECT * FROM member WHERE username = %s", (account,))
  result = cursor.fetchone()
  return result is not None

# 檢查帳號密碼是否吻合已註冊之會員資料
def check_member(account, password):
  cursor.execute("SELECT * FROM member WHERE (username, password) = (%s, %s)", (account, password))
  result = cursor.fetchone()
  return result is not None

# 新增帳號到資料庫
def add_account(name, account, password):
    cursor.execute("INSERT INTO member (name, username, password) VALUES (%s, %s, %s)", (name, account, password))
    con.commit()

# 使用 GET 方法(預設)，處理路徑 / 的對應函式
@app.route("/")
def index(): # 用來回應網站首頁連線的函式
  return render_template('index.html')# 回傳網站首頁的內容

# 建立路徑 /signup 對應的處理函式，註冊區域
@app.route("/signup", methods=['POST'])
def signup():
  name = request.form["signupName"]
  account = request.form["signupAccount"]
  password = request.form["signupPassword"]
  if check_account(account):
    return redirect(url_for('error', message='帳號已經被註冊'))
  else:
    add_account(name, account, password)
    return redirect(url_for('index'))

# 建立路徑 /signin 對應的處理函式，登入區域
@app.route("/signin", methods=['POST'])
def signin():
  account = request.form["signinAccount"]
  password = request.form["signinPassword"]
  if check_member(account, password):
    session["sign_in"] = True
    cursor.execute("SELECT name FROM member WHERE username = %s", (account,))
    result = cursor.fetchone()
    name = result[0]  # 取得名稱
    session['name'] = name
    return redirect(url_for('member'))
  else:
    return redirect(url_for('error', message='帳號或密碼輸入錯誤'))

# 建立路徑 /member 對應的處理函式
@app.route("/member")
def member():
  if session["sign_in"] == True:
    name = session.get('name', '')  # 從 session 中取得姓名
    cursor.execute("SELECT member.name, message.content, message.id FROM member INNER JOIN message ON member.id = message.member_id ORDER BY message.id DESC")
    contentList = cursor.fetchall()
    return render_template('member.html', name=name, contentList=contentList)
  else:
    return redirect(url_for('index'))

# 建立路徑 /createMessage 對應的處理函式
@app.route("/createMessage", methods=['POST'])
def createMessage():
  content = request.form["content"]
  name = session.get('name', '')
  cursor.execute("SELECT id FROM member WHERE name = %s", (name,))
  memberId = cursor.fetchone()[0]
  cursor.execute("INSERT INTO message(member_id, content) values (%s, %s)", (memberId, content))
  con.commit()  # 確定執行資料庫操作
  return redirect(url_for('member'))

# 建立路徑 /deleteMessage 對應的處理函式
@app.route("/deleteMessage/<int:contentId>")
def deleteMessage(contentId):  
  cursor.execute("DELETE FROM message WHERE id = %s", (contentId,))
  con.commit()  # 確定執行資料庫操作
  return redirect(url_for('member'))

# 建立路徑 /error 對應的處理函式
@app.route("/error")
def error():
  message = request.args.get('message', '')
  return render_template('error.html', message=message)

# 建立路徑 /signout 對應的處理函式
@app.route("/signout")
def signout():
  session["sign_in"] = False
  return redirect(url_for('index'))

# 啟動網站伺服器
app.run(port=3000)