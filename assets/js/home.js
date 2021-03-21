window.audioHasPlayed = false;
window.shouldPlayAudio = !JSON.parse(localStorage.getItem("audioDisabled"));
document.body.onclick = () => {
  if (!window.audioHasPlayed && window.shouldPlayAudio)
    document.querySelector("audio").play();
  window.audioHasPlayed = true;
};

window.audioControlsMenuOpen = false;
document.querySelector(".audioControls span").onclick = () => {
  if (window.audioControlsMenuOpen) {
    document.querySelector("body").style.justifyContent = "";
    document.querySelector("main").style.display = "";
    document.querySelector(".audioControlMenu").style.display = "none";
  } else {
    document.querySelector("body").style.justifyContent = "center";
    document.querySelector("main").style.display = "none";
    document.querySelector(".audioControlMenu").style.display = "unset";
  }
  window.audioControlsMenuOpen = !window.audioControlsMenuOpen;
};

document.querySelector(".switch input").checked = !window.shouldPlayAudio;
document.querySelector(".switch input").onclick = () => {
  window.shouldPlayAudio = !window.shouldPlayAudio;
  localStorage.setItem("audioDisabled", !window.shouldPlayAudio);
};
