function showSomething(selector) {
  document.querySelector("#mainLayout").setAttribute("hidden", "");
  document.querySelector("#chatLayout").setAttribute("hidden", "");
  document.querySelector("#scanLayout").setAttribute("hidden", "");
  document.querySelector(selector).removeAttribute("hidden");
}
document.querySelector(".scan-button").onclick = () => {
  showSomething("#scanLayout");
}
document.querySelector(".chat-button").onclick = () => {
  showSomething("#chatLayout");
}
document.querySelectorAll(".close-button").forEach((el) => {
  el.onclick = () => {
    showSomething("#mainLayout")
  }
});
