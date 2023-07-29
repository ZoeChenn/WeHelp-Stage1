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

button.addEventListener("click", (e) => {
  let formNum = num.value
  let newPath = "/square/" + String(formNum);

  if (num.value > 0){
    console.log(num.value)
    window.location.href = newPath;
    e.preventDefault() // 避免表單執行預設提交行為，才能將新網址貼到網址列去作用
  }else {
    alert("Please enter a positive number")
    e.preventDefault()
    num.value = ''
  }
});