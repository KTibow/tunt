function preloadImage(source) {
  var imageObj = new Image();
  imageObj.src = source;
}
function getCardsReady(howManyCards) {
  var randomIds = [];
  var currentRow = document.createElement("div");
  currentRow.classList.add("row");
  for (var i = 0; i < howManyCards; i++) {
    var cardClone = document.querySelector("template").content.cloneNode(true);
    var cardId;
    do {
      cardId = Math.floor(Math.random() * 5 * howManyCards);
    } while (randomIds.includes(cardId));
    randomIds.push(cardId);
    // Fill in QR code
    var imageSource = `https://bwipjs-api.metafloor.com/?bcid=qrcode&text=${cardId}`;
    cardClone.querySelector("img").src = imageSource;
    preloadImage(imageSource);
    preloadImage.src = cardClone.querySelector("img").src;
    // Add element
    currentRow.appendChild(cardClone);
    if (currentRow.childElementCount == 4) {
      document.querySelector(".printShow").appendChild(currentRow);
      currentRow = document.createElement("div");
      currentRow.classList.add("row");
    }
  }
  if (currentRow.childElementCount > 0) {
    document.querySelector(".printShow").appendChild(currentRow);
  }
  return randomIds;
}
window.onbeforeprint = () => {
  alert("Make sure to check Background graphics in the settings.");
};
function createCards() {
  var cardNumber = document.querySelector("input").value;
  getCardsReady(cardNumber);
  // Wait for images to load
  setTimeout(window.print, cardNumber * 50);
}
