# -*- coding: utf-8 -*-
# === Task1 ===
import urllib.request as request
import json
import csv
import ssl

def get_data_from_api(api_url):
  try:
    # 忽略 SSL 驗證
    ssl._create_default_https_context = ssl._create_default_https_context = ssl._create_unverified_context

    response = request.urlopen(api_url)
    data = json.loads(response.read())
    return data
  except Exception as e:
    print(f"Error while fetching data: {e}")
    return None

def save_to_attraction_csv(data, file_path):
  try:
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerow(["景點名稱", "區域", "經度","緯度","第一張圖檔網址"])

      for attraction in data["result"]["results"]:
        name = attraction["stitle"]
        area = attraction["address"][5:8]
        longitude = attraction["longitude"]
        latitude = attraction["latitude"]
        imgAddress = ("https" + attraction["file"].split("https")[1])
        writer.writerow([name, area, longitude, latitude, imgAddress])
    print(f"資料已成功寫入 {file_path}")
  except Exception as e:
    print(f"寫入 {file_path} 時發生錯誤：{e}")

def save_to_mrt_csv(data, file_path):
  try:
    mrt_dict = {}
    for attraction in data["result"]["results"]:
      mrt = attraction["MRT"]
      if mrt:
        if mrt not in mrt_dict:
          mrt_dict[mrt] = []
        mrt_dict[mrt].append(attraction["stitle"])

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
      csvfile.write("捷運站名稱,景點名稱\n")

      for mrt, attractions in mrt_dict.items():
          attractions_str = ','.join(attractions)
          csvfile.write(f"{mrt},{attractions_str}\n")
    print(f"資料已成功寫入 {file_path}")
  except Exception as e:
    print(f"寫入 {file_path} 時發生錯誤：{e}")

# API 網址
api_url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

# 呼叫函式發送 API 請求並取得回應資料
api_data = get_data_from_api(api_url)

# 若成功取得資料，將資料寫入 CSV 檔案
if api_data:
  attraction_csv_file = "attraction.csv"
  mrt_csv_file = "mrt.csv"
  save_to_attraction_csv(api_data, attraction_csv_file)
  save_to_mrt_csv(api_data, mrt_csv_file)



# === Task2 ===
import urllib.request as req

def get_post_time(perPageURL):
  # 建立一個 Request 物件，附加 Request Headers 的資訊讓自己看起來像一般使用者
  request = req.Request(perPageURL, headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  })
  with req.urlopen(request) as response:
    data =  response.read().decode("utf-8")
  # 使用 BeautifulSoup 解析原始碼，取得每篇文章的標題
  import bs4
  root = bs4.BeautifulSoup(data, "html.parser")
  postTimeSet = root.find_all("span", class_="article-meta-value") # 尋找所有 class_="article-meta-value" 的 span 標籤
  for postTime in postTimeSet:
    eachPostTime = postTime.text # 提取發文時間
  return eachPostTime

def get_data(url):
  # 建立一個 Request 物件，附加 Request Headers 的資訊讓自己看起來像一般使用者
  request = req.Request(url, headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  })
  with req.urlopen(request) as response:
    data =  response.read().decode("utf-8")

  # 使用 BeautifulSoup 解析原始碼，取得每篇文章的標題
  import bs4
  root = bs4.BeautifulSoup(data, "html.parser")
  # find 找單一；find_all 找所有符合的項目，並以 List 方式列出來
  titles = root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
  pushNum = root.find_all("div", class_="nrec")

  # 創建 movie.txt 檔案， a 是附加的意思，若檔案已經存在，資料會被附加在檔案內容的末尾，而不是覆寫原有的內容
  with open("movie.txt", "a", encoding="utf-8") as file:
    for title, nrec in zip(titles, pushNum): # 遍歷 titles、pushNum 去跑
      if title.a != None: # 剔除沒有 a 標籤（被刪除）的內容
        eachTitle = title.a.string # 取出其中的標題文字
        perPageURL = "https://www.ptt.cc" + title.a["href"] # 取出該標題的網址
      span = nrec.find("span")
      eachPushNum = span.text if span else "0" # 取出 span 中的文字，無則顯示 0
      eachPostTime = get_post_time(perPageURL) # 用該標題網址呼叫 get_post_time 函式進去提取發文時間
    
      # 將資料寫入檔案
      file.write(f"{eachTitle},{eachPushNum},{eachPostTime}\n")

  nextLink = root.find("a", string = "‹ 上頁") # 找到內文是 "‹ 上頁" 的 a 標籤，並抓取
  return nextLink["href"] # 資料長相：/bbs/movie/index9624.html

pageURL = "https://www.ptt.cc/bbs/movie/index.html" # 電影版首頁
count = 0
while count < 3: # 找三頁
  pageURL = "https://www.ptt.cc" + get_data(pageURL)
  count+=1