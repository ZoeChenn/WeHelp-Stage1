## 要求三：SQL CRUD
### 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
![截圖 2023-08-01 14 54 10](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/b87c8040-81c1-49c9-bde5-20338357feb5)
![截圖 2023-08-01 14 55 15](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/498ada39-7b2a-4f50-87c1-b67aac378831)
![截圖 2023-08-01 14 55 34](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/2c61a5c2-9d53-496a-8449-6dad93c348e1)

### 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![截圖 2023-08-01 14 55 51](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/7a52f2a9-c833-4f21-8371-6c153a064471)

### 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
![截圖 2023-08-01 14 56 13](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/a9c4a96a-a438-4426-a81d-3d6906f10317)

### 使用 SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
![截圖 2023-08-01 14 56 44](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/945576f2-0dde-4f79-a1d4-76cd6273772f)

### 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![截圖 2023-08-01 15 00 08](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/bea91120-05a9-4e77-956d-2d86d48fdeb6)

### 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![截圖 2023-08-01 15 02 14](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/13b82e1a-ea0e-4e1e-bcc4-9c117a80a8c5)

### 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。 
![截圖 2023-08-01 15 04 18](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/945afac6-9418-4c51-b610-d26324e9b8cb)
![截圖 2023-08-01 15 06 45](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/27129d42-f556-4f88-b7a7-a7ca3ab821b7)


## 要求四：SQL Aggregate Functions
![截圖 2023-08-01 15 16 00](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/6e0a157e-d73a-4a59-8e98-d8487a754a13)

### 取得 member 資料表中，總共有幾筆資料（幾位會員）。
![截圖 2023-08-01 15 22 49](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/ce1dacaf-f928-420d-a155-770bfa6e4a16)

### 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![截圖 2023-08-01 15 21 29](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/e58b9b35-1420-4d44-aaea-bf75287bfea7)

### 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![截圖 2023-08-01 15 21 45](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/e686198e-34e4-45d7-9743-010b9a952b6e)


## 要求五：SQL JOIN
![截圖 2023-08-01 15 53 43](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/2db0f079-4e9d-47eb-a0d6-370f53cdd1e7)

### 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者的姓名。
![截圖 2023-08-01 17 11 08](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/dc731d43-1b31-42ae-98ae-aa543427c096)

### 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者的姓名。
![截圖 2023-08-01 17 15 59](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/f25644a2-b122-4b2a-948c-3cfb350d7101)

### 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
![截圖 2023-08-01 17 27 12](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/8a672cd0-853a-4c87-b9f8-ec249f4374a8)
![截圖 2023-08-01 17 27 21](https://github.com/ZoeChenn/WeHelp-Stage1/assets/96377193/d80ae545-3330-4d5d-857e-ce0c9adc56d1)
