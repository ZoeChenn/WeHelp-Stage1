// 漢堡選單
const hamburgerMenu = document.querySelector('.mobileOpen');
const asideMenu = document.querySelector('.aside');
// console.log(hamburgerMenu)
// console.log(asideMenu)

hamburgerMenu.addEventListener('click', (e) => {
  asideMenu.classList.toggle('showMenu');
  // console.log("hello")
  // console.log(asideMenu)
});

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

fetch(src).then(function(response){
	return response.json();
}).then(function(data){
	renderData(data.result.results); //JSON格式資料
  console.log(data.result.results)
}).catch(function(error){
  console.log("發生錯誤" + error);
});

function renderData(data) {
  const cards = document.querySelector(".cards");
  let titleCount = 0;
  
  data.forEach(function(attraction,index) {
  // 創建外層的 <div> 元素
  const cardDiv = document.createElement("div");
  
  // 根據索引值判斷要套用的類別
  if (index < 3) {
    cardDiv.classList.add("card-promo");
  } else {
    if (titleCount >= 12) {
      return; // 超過 12 筆 "card-title" 就結束函式執行
    }
    cardDiv.classList.add("card-title");
    titleCount++;
  }

  // 創建圖片元素 <img> 並設定 src 和 alt 屬性
  const img = document.createElement("img");
  img.src = "https" + attraction.file.split("https")[1];
  img.alt = "";

  // 創建包含標題的 <div> 元素
  const imgDiv = document.createElement("div");
  imgDiv.classList.add("imgDiv");

  // 創建包含標題的 <div> 元素
  const contentDiv = document.createElement("div");
  contentDiv.classList.add("content");
  
  // 創建標題元素 <h3> 並設定標題文字
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
}

