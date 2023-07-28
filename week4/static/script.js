const submit = document.querySelector("#submit")
const agree = document.querySelector("#agree")
const num = document.querySelector("#num")
const button = document.querySelector("#button")

agree.addEventListener('click', ()=>{
  // console.log(agree.value)
  if (agree.value === 'false'){
    agree.value = 'true'
  }else {
    agree.value = 'false'
  }
})

submit.addEventListener('click', (e)=>{
  if (agree.value !== 'true'){
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