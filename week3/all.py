# -*- coding: utf-8 -*-
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
