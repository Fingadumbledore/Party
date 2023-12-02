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



function openPopup() {
  document.getElementById('gamePopup').style.display = 'block';
  document.getElementById('overlay').style.display = 'block';
}

var games = [
  {
    "Name": "Tomb Raider",
    "Teil": 3,
    "Erscheinungsjahr": 1998,
    "Genre": "Abenteuer",
    "Publisher": "Core Design",
    "Inhalt": "Tomb Raider III – Adventures of Lara Croft ist ein Videospiel aus der Reihe Tomb Raider. Es wurde von Core Design entwickelt und erschien im Winter 1998 für die PlayStation und den PC. Lara hat wieder einiges dazugelernt.",
    "Bild": "./static/img/tombraider.png"
  },
  {
    "Name": "Need For Speed Underground",
    "Teil": 2,
    "Erscheinungsjahr": 2004,
    "Genre": "Autorennen",
    "Publisher": "EA",
    "Inhalt": "Need for Speed: Underground 2 ist der achte Teil der von Electronic Arts entwickelten Rennspielserie Need for Speed und erschien am 18. November 2004 für Windows, PS2, Xbox, GameCube, GBA und Nintendo DS. Die Version für PSP wurde je nach Veröffentlichungsregion zwischen Januar und September 2005 veröffentlicht.",
    "Bild": "./static/img/nfsu2.png"
  },
  {
    "Name": "Anno",
    "Teil": "1602",
    "Erscheinungsjahr": 1998,
    "Genre": "Echtzeitstrategie",
    "Publisher": "Sunflowers",
    "Inhalt": "Anno 1602 ist das erste Computerspiel aus der Anno-Serie. Das Spiel entstand aus einem Gemeinschaftsprojekt des österreichischen Spieleentwicklers Max Design und der deutschen Sunflowers Interactive Entertainment Software GmbH.",
    "Bild": "./static/img/anno.png"
  },
  {
    "Name": "Empire Earth",
    "Teil": 1,
    "Erscheinungsjahr": 2001,
    "Genre": "Echtzeitstrategie",
    "Publisher": "Sierra Entertainment",
    "Inhalt": "Empire Earth ist eine dreiteilige Echtzeit-Strategiespiel-Serie für Windows, in der der Spieler eine Zivilisation durch die gesamte Menschheitsgeschichte führen kann.",
    "Bild": "./static/img/empire.png"
  },
  {
    "Name": "Call Of Duty 4 Modern Warfare",
    "Teil": 4,
    "Erscheinungsjahr": 2007,
    "Genre": "Shooter",
    "Publisher": "Infinity Ward",
    "Inhalt": "In der Call-of-Duty-Reihe wird erstmals eine zusammenhängende Handlung erzählt. Ein russischer Ultranationalist und ein Terrorist übernehmen die Kontrolle in einem arabischen Staat. Eine amerikanische und britische Einheit jagt sie, es kommt zu einem Atomangriff. Der russische Ultranationalist startet nukleare Raketen, die in letzter Sekunde zerstört werden. Am Ende tötet der Spieler den russischen Ultranationalisten und wird gerettet. Es gibt auch eine Bonusmission, in der ein Flugzeugabsturz verhindert wird.",
    "Bild": "./static/img/cod.png"
  }
];

var currentGameIndex = 0;

function openPopup() {
  showGameInfo(currentGameIndex);
  document.getElementById('gamePopup').style.display = 'block';
  document.getElementById('overlay').style.display = 'block';
}

function closePopup() {
  document.getElementById('gamePopup').style.display = 'none';
  document.getElementById('overlay').style.display = 'none';
}

function showGameInfo(index) {
  var game = games[index];
  document.getElementById('popupImage').src = game.Bild;
  document.getElementById('popupTitle').innerHTML = game.Name;
  document.getElementById('popupYear').innerHTML = 'Erscheinungsjahr: ' + game.Erscheinungsjahr;
  document.getElementById('popupGenre').innerHTML = 'Genre: ' + game.Genre;
  document.getElementById('popupPublisher').innerHTML = 'Publisher: ' + game.Publisher;
  document.getElementById('popupContent').innerHTML = game.Inhalt;
}

function prevGame() {
  currentGameIndex = (currentGameIndex - 1 + games.length) % games.length;
  showGameInfo(currentGameIndex);
}

function nextGame() {
  currentGameIndex = (currentGameIndex + 1) % games.length;
  showGameInfo(currentGameIndex);
}