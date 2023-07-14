/* Task1 */
function findAndPrint(messages) {
  console.log("====Task1====");
  const above17 = ['18', 'college', 'legal', 'vote'];
  for (let name in messages) {
    for (let i = 0; i < above17.length; i++) {
      if (messages[name].includes(above17[i])) {
        console.log(name);
        break;
      }
    }
  }
  }
findAndPrint({
  "Bob":"My name is Bob. I'm 18 years old.",
  "Mary":"Hello, glad to meet you.",
  "Copper":"I'm a college student. Nice to meet you.",
  "Leslie":"I am of legal age in Taiwan.",
  "Vivian":"I will vote for Donald Trump next week",
  "Jenny":"Good morning."
});

/*-------------------------------------------------*/

/* Task2 */
function calculateSumOfBonus(data) {
  console.log("====Task2====");
  sum = 0;
  for (let employee of data["employees"]) {
    let salary = 0;
    if (typeof employee["salary"] === "string") {
      if (employee["salary"].includes("USD")) {
        salary = parseInt(employee["salary"].replace("USD", ""))*30;
        // John 的薪水
      } else {
        salary = parseInt(employee["salary"].replace(",", ""));
        // Jenny 的薪水
      }
    } else {
      salary = parseInt(employee["salary"]);
      // Bob 的薪水
    }

    const performance = employee["performance"]; // 判別表現

    let bonus = 0;
    if (performance === "above average") {
      bonus = salary * 0.08;
    } else if (performance === "average") {
      bonus = salary * 0.05;
    } else if (performance === "below average") {
      bonus = salary * 0.03;
    }

    const role = employee["role"]; // 判別角色加乘

    if (role === "Engineer") {
      bonus += 500;
    } else if (role === "CEO") {
      bonus += 1000;
    } else if (role === "Sales") {
      bonus += 500;
    }
      sum = sum + bonus;
  }
  console.log(sum);
}

calculateSumOfBonus({
  "employees": [
    {
      "name": "John",
      "salary": "1000USD",
      "performance": "above average",
      "role": "Engineer"
    },
    {
      "name": "Bob",
      "salary": 60000,
      "performance": "average",
      "role": "CEO"
    },
    {
      "name": "Jenny",
      "salary": "50,000",
      "performance": "below average",
      "role": "Sales"
    }
  ]
});

/*-------------------------------------------------*/

/* Task3 */
function func(...data){
  for (i=0 ; i<data.length ; i++) {
    const string = data[i]
    if (string.length >= 2) {
      const secondWord = string[1];
      let unique = true;
      for (e=0 ; e<data.length ; e++) {
        if (i!=e && data[e].length >= 2 && data[e][1]===secondWord) {
          unique = false;
          break
        }
      }
      if (unique) {
        console.log(string);
        return
      }
    }
  }
  console.log("沒有");
}
console.log("====Task3====");
func("彭大牆", "王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有

/*-------------------------------------------------*/

/* Task4 */
function getNumber(index){
  let numberList = [0, 4]; // 先建立初始值
  while (numberList.length <= index) {
    // 若輸入的索引小於數列長度，就進入生成器
    numberList.push(numberList[numberList.length - 2] + 3);
    // 持續以倒數第二個數字 +3 來生成數列，直到數列長度大於索引
  }
  console.log(numberList[index]);
}
console.log("====Task4====");
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15