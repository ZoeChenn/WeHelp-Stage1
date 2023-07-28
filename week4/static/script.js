const submit = document.querySelector("#submit")
const agree = document.querySelector("#agree")
const num = document.querySelector("#num")
const button = document.querySelector("#button")

submit.addEventListener('click', (e)=>{
  console.log(agree.checked)
  if (!agree.checked){
    alert("Please check the checkbox first")
    e.preventDefault()
  }
})

button.addEventListener('click', (e)=>{
  if (num.value > 0){
    console.log(num.value)
  }else {
    alert("Please enter a positive number")
    e.preventDefault()
    num.value = ''
  }
})

button.addEventListener("click", (e) => {
  // console.log(num.value)
  let formNum = num.value
  let newPath = "/square/" + String(formNum);
  // console.log(newPath)
  window.location.href = newPath;
  // console.log(window.location.href)
  e.preventDefault() // 避免表單執行預設提交行為，才能將新網址貼到網址列去作用
});