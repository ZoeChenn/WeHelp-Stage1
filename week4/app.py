from flask import Flask # 載入 Flask
from flask import request
from flask import redirect, url_for
from flask import render_template
from flask import session
app = Flask( # 建立 Application 物件
  __name__, # 靜態檔案的資料夾名稱
  static_folder='static',
  static_url_path='/',
  template_folder='templates',
) # 所有在 static 資料夾底下的檔案，都對應到網址路徑 /static/檔案名稱

app.secret_key="any string but secret" # 設定 Session 密鑰

# 使用 GET 方法(預設)，處理路徑 / 的對應函式
@app.route("/")
def index(): # 用來回應網站首頁連線的函式
  return render_template('index.html')# 回傳網站首頁的內容

# 建立路徑 /signin 對應的處理函式
@app.route("/signin", methods=['POST'])
def signin():
  account = request.form["account"]
  password = request.form["password"]
  if account == "test" and password == "test":
    session["sign_in"] = True
    return redirect(url_for('member'))
  elif account == "" or password == "":
    return redirect(url_for('error', message='請輸入帳號、密碼'))
  else: 
    return redirect(url_for('error', message='帳號或密碼輸入錯誤'))

# 建立路徑 /member 對應的處理函式
@app.route("/member")
def member():
  if session["sign_in"] == True:
    return render_template('member.html')
  else:
    return redirect(url_for('index'))

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

# 建立路徑 /square 對應的處理函式
@app.route("/square")
def square():
  num = request.args.get('num', '')
  # return redirect(f"/square/{num}")
  return redirect("/square/" + num)

# 建立路徑 /square/<int:num> 對應的處理函式
@app.route("/square/<int:num>")
def displaySquare(num):
  num = int(num)
  squareNum = num * num
  return render_template("square.html", data=squareNum)

# 啟動網站伺服器
app.run(port=3000)