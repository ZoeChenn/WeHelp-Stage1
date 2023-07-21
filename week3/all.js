// 漢堡選單事件
const hamburgerMenu = document.querySelector('.mobileOpen');
const asideMenu = document.querySelector('.aside');
// console.log(hamburgerMenu)
// console.log(asideMenu)
hamburgerMenu.addEventListener('click', (e) => {
  asideMenu.classList.toggle('showMenu'); // 點擊後開關浮動選單
  // console.log("hello")
  // console.log(asideMenu)
});

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
let allData; // 讓資料成為全域變數
let renderCount = 0; // 計算總共渲染幾筆資料

fetch(src).then(function(response){
	return response.json();
})
  .then(function(data){
    allData = data.result.results // JSON格式資料
    renderData(allData); // 連結成功就直接執行渲染 
    // console.log(allData)
})
  .catch(function(error){
    console.log("發生錯誤" + error);
});

// 按鈕點擊事件
const button = document.querySelector("button");
button.addEventListener('click', () => {
  const dataToRender = allData.slice(renderCount, renderCount + 12); // 渲染 x+1 到 x+12 筆資料，避免重複
  renderData(dataToRender);
  renderCount += 12; // 渲染筆數 + 12
  // console.log("有按到");
  // console.log('點擊後的renderCount是'+renderCount)
});

// 渲染頁面函式
function renderData(data) {
  const cards = document.querySelector(".cards");
  let titleCount = 0; // 紀錄 "card-title" 渲染了幾個
  
  data.forEach(function(attraction,index) {
  // 創建卡片 div
  const cardDiv = document.createElement("div"); 
  
  // 判斷若未渲染過且為前三筆資料，套用 "card-promo" 樣式，其餘皆套用 "card-title" 樣式
  if (renderCount === 0 && index < 3) {
    cardDiv.classList.add("card-promo");
  } else {
    // 超過 12 筆 "card-title" 就結束函式執行
    if (titleCount >= 12) {
      return; 
    }
    cardDiv.classList.add("card-title");
    titleCount++;
    // console.log("有印製");
  }

  // 創建 <img> 並設定 src 和 alt 屬性
  const img = document.createElement("img");
  img.src = "https" + attraction.file.split("https")[1]; // 以 https 為節點做分割，取第一筆，並把文字 https 加回去
  img.alt = "";

  // 創建包照片的 <div>
  const imgDiv = document.createElement("div");
  imgDiv.classList.add("imgDiv");

  // 創建包含標題的 <div>
  const contentDiv = document.createElement("div");
  contentDiv.classList.add("content");
  
  // 創建 <h3> 並設定標題文字
  const h3 = document.createElement("h3");
  h3.textContent = attraction.stitle;

  // 將 img 成為 imgDiv 的子層
  imgDiv.appendChild(img);
  
  // 將 h3 成為 contentDiv 的子層
  contentDiv.appendChild(h3);

  // 將 imgDiv 及 contentDiv 成為 cardDiv 的子層
  cardDiv.appendChild(imgDiv);
  cardDiv.appendChild(contentDiv);
  
  // 將 cardDiv 成為 container 的子層
  cards.appendChild(cardDiv);
  });

  // 若未渲染過，renderCount+15，排除掉首次渲染的 15 筆資料，讓後續維持增加 12 筆
  if (renderCount === 0) {
    renderCount+=15;
  }
  // console.log('入函式後的renderCount是'+renderCount)
}
