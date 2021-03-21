window.audioHasPlayed = false;
window.shouldPlayAudio = !JSON.parse(localStorage.getItem("audioDisabled"));
document.body.onclick = () => {
  if (!window.audioHasPlayed && window.shouldPlayAudio)
    document.querySelector("audio").play();
  window.audioHasPlayed = true;
};

document.querySelector(".audioControls span").onclick = () => {
  document.querySelector("body").style.justifyContent = "center";
  document.querySelector("main").style.display = "none";
  document.querySelector(".audioControlMenu").style.display = "unset";
};

document.querySelector(".switch input").checked = !window.shouldPlayAudio;
document.querySelector(".switch input").onclick = () => {
  window.shouldPlayAudio = !window.shouldPlayAudio;
  localStorage.setItem("audioDisabled", !window.shouldPlayAudio);
};
