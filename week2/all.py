# -*- coding: utf-8 -*-

# # Task1
def find_and_print(messages):
  print("====Task1====")
  above17 = ['18', 'college', 'legal', 'vote']
  for name, message in messages.items():
    for keyword in above17:
      if keyword in message:
        print(name)
        break

find_and_print({
  "Bob":"My name is Bob. I'm 18 years old.",
  "Mary":"Hello, glad to meet you.",
  "Copper":"I'm a college student. Nice to meet you.",
  "Leslie":"I am of legal age in Taiwan.",
  "Vivian":"I will vote for Donald Trump next week",
  "Jenny":"Good morning."
})

######################################################

# # Task2
def calculate_sum_of_bonus(data):
  print("====Task2====")
  sum = 0
  for employee in data["employees"]:
    if isinstance(employee["salary"], str): # 判斷薪水型態是否為字串
      if "USD" in employee["salary"]:
        salary = int(employee["salary"].replace("USD", ""))*30
        # John 的薪水
      else:
        salary = int(employee["salary"].replace(",", ""))
        # Jenny 的薪水
    else:
      salary = int(employee["salary"])
      # Bob 的薪水

    performance = employee["performance"] # 判別表現

    if performance == "above average":
      bonus = salary * 0.08
    elif performance == "average":
      bonus = salary * 0.05
    elif performance == "below average":
      bonus = salary * 0.03
    else:
      bonus = 0

    role = employee["role"] # 判別角色加乘

    if role == "Engineer":
      bonus = int(bonus + 500)
    elif role == "CEO":
      bonus = int(bonus + 1000)
    elif role == "Sales":
      bonus = int(bonus + 500)
    else:
      bonus = 0
    sum = sum + bonus
  print(sum) 

calculate_sum_of_bonus({ 
  "employees":[
    {
      "name":"John",
      "salary":"1000USD", 
      "performance":"above average", 
      "role":"Engineer"
    },
    {
      "name":"Bob", 
      "salary":60000,
      "performance":"average",
      "role":"CEO"
    },
    {
      "name":"Jenny",
      "salary":"50,000",
      "performance":"below average",
      "role":"Sales"
    } 
  ]
}) # call calculate_sum_of_bonus function

######################################################

# # Task3
def func(*data):
  for i, string in enumerate(data):
    if len(string) >= 2:
      SecondWord = string[1]
      unique = True # 先獨立出第二個字
      for i2, string2 in enumerate(data):
        if i != i2 and len(string2) >= 2 and string2[1] == SecondWord:
          unique = False # 確定不是同一個字串，但第二個字相同，獨特性變成 False
          break
      if unique: # if 獨特性 = True，印出字串
        print(string)
        return
  print('沒有') # 獨特性 = False，則印出沒有

print("====Task3====")
func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

######################################################

# # Task4
def get_number(index):
  NumberList = [0, 4] # 先建立初始值
  while len(NumberList) <= index: # 若輸入的索引小於數列長度，就進入生成器
    NumberList.append(NumberList[-2] + 3) # 持續以倒數第二個數字 +3 來生成數列，直到數列長度大於索引
  print(NumberList[index])

print("====Task4====")
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15