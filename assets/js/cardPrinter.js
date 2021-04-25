function getCardsReady(howManyCards) {
  var randomIds = [];
  for (var i = 0; i < howManyCards; i++) {
    var cardClone = document.querySelector("template").content.cloneNode(true);
    var cardId;
    do {
      cardId = Math.floor(Math.random() * 5 * howManyCards);
    } while (randomIds.includes(cardId));
    randomIds.push(cardId);
    cardClone.querySelector(
      "img"
    ).src = `https://bwipjs-api.metafloor.com/?bcid=qrcode&text=${cardId}`;
    document.querySelector(".printShow").appendChild(cardClone);
  }
  return randomIds;
}
