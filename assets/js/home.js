window.onload = () => {
  document.body.onclick = () => {
    document.querySelector("audio").play();
  };
}
window.onload();
document.querySelector(".audioControls span").onclick = () => {
  document.querySelector("body").style.justifyContent = "center";
  document.querySelector("main").style.display = "none";
  document.querySelector(".audioControlMenu").style.display = "unset";
}
