const socket = io();

window.addEventListener('DOMContentLoaded', function() {
    var name = sessionStorage.getItem('name'); // Den Namen aus dem SessionStorage abrufen

    if (name) {
      document.getElementById('peter').textContent = name; // Den Namen bei dem Element mit der ID "peter" ausgeben
    }
  });

  var divs = document.querySelectorAll('.hidden-div');
  var activeButtonIndex = null;
  
  // Beim Laden der Seite den Zustand wiederherstellen
  window.addEventListener('DOMContentLoaded', function() {
    var storedIndex = sessionStorage.getItem('position');
    if (storedIndex) {
      activeButtonIndex = parseInt(storedIndex);
      toggleDiv(activeButtonIndex);
    }
  });
  
  function toggleDiv(index) {
    updateButtonStatus(index);
    hideAllDivs();
    
    var selectedIndex = index - 1;
    handleSwitchDiv(index);
    
    divs[selectedIndex].style.display = 'block';
  
    // Index im Session Storage speichern
    sessionStorage.setItem('position', index);
  }
  
  function hideAllDivs() {
    for (var i = 0; i < divs.length; i++) {
      divs[i].style.display = 'none';
    }
  }
  
  function updateButtonStatus(index) {
    for (var i = 0; i < divs.length; i++) {
      var button = document.getElementsByClassName('seitenbutton')[i];
      button.classList.remove('active-button');
    }
  
    var activeButton = document.getElementsByClassName('seitenbutton')[index - 1];
    activeButton.classList.add('active-button');
  }
  
  function togglePopup() {
    var popup = document.getElementById("popup");
    popup.style.display = (popup.style.display === "none") ? "block" : "none";
}

function handleSwitchDiv(index) {
    // reset divs
    // 1. reset mate div
    var mate_kiste = document.getElementById('mate_kiste');
    mate_kiste.innerHTML = '';

    switch (index) {
        case 4:
            // get previous messages
            getNChatMessages(socket, 100, 0);
            break;
        case 6: // Mate
            getMateStatus(socket);
            break;
    }
}

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

function showDiv(divId) {
  const divToShow = document.getElementById(divId);
  const divs = document.querySelectorAll('div');

  for (const div of divs) {
      div.classList.add('hidden');
  }

  divToShow.classList.remove('hidden');
}


