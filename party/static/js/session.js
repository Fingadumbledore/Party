const socket = io();

function skipSong() {}
function lastSong() {}
function pausePlaySong() {}

function updateClock() {
  var now = new Date();
  var hours = now.getHours();
  var minutes = now.getMinutes();

  // Führende Nullen hinzufügen, wenn die Stunden oder Minuten einstellig sind
  if (hours < 10) {
      hours = "0" + hours;
  }
  if (minutes < 10) {
      minutes = "0" + minutes;
  }

  var timeString = hours + ":" + minutes;

  document.getElementById("uhrzeit").innerHTML = timeString;
}

setInterval(updateClock, 1000);
