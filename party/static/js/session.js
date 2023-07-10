window.addEventListener('DOMContentLoaded', function() {
    var name = sessionStorage.getItem('name'); // Den Namen aus dem SessionStorage abrufen

    if (name) {
      document.getElementById('peter').textContent = name; // Den Namen bei dem Element mit der ID "peter" ausgeben
    }
  });

// Array zum Speichern der Div-Elemente
var divs = document.querySelectorAll('.hidden-div');
// Aktuell ausgewählter Button-Index
var activeButtonIndex = null;

// Funktion zum Umschalten der Div-Elemente
function toggleDiv(index) {
    // Button-Status aktualisieren
    updateButtonStatus(index);

    // Alle Div-Elemente ausblenden
    hideAllDivs();

    // Index des gewählten Div-Elements
    var selectedIndex = index - 1;

    handleSwitchDiv(index);

    // Gewähltes Div-Element einblenden
    divs[selectedIndex].style.display = 'block';
}

// Funktion zum Ausblenden aller Div-Elemente
function hideAllDivs() {
    for (var i = 0; i < divs.length; i++) {
        divs[i].style.display = 'none';
    }
}

// Funktion zum Aktualisieren des Button-Status
function updateButtonStatus(index) {
    // Button-Klassen entfernen
    for (var i = 0; i < divs.length; i++) {
        var button = document.getElementsByClassName('seitenbutton')[i];
        button.classList.remove('active-button');
    }

    // Aktuellen Button hervorheben
    var activeButton = document.getElementsByClassName('seitenbutton')[index - 1];
    activeButton.classList.add('active-button');
}

  function togglePopup() {
    var popup = document.getElementById("popup");
    popup.style.display = (popup.style.display === "none") ? "block" : "none";
}

function handleSwitchDiv(index) {
    switch (index) {
        case 6: // Mate
            var mate_kiste = document.getElementById('mate_kiste');
            var table = document.createElement('tbody');
            
            for (let rowNumber = 0; rowNumber < 4; rowNumber++) {
                const row = document.createElement('tr');

                for (let columnNumber = 0; columnNumber < 5; columnNumber++) {
                    const cell = document.createElement('td');
                    const flascheTrinkenButton = document.createElement('button');
                    flascheTrinkenButton.onclick = () => flascheTrinken(rowNumber, columnNumber);

                    flascheTrinkenButton.classList.add('flasche-trinken-button');
                    flascheTrinkenButton.id = `flasche-trinken-button-${rowNumber}-${columnNumber}`;
                    cell.appendChild(flascheTrinkenButton);

                    row.appendChild(cell);
                }
                table.appendChild(row);            
            }
            mate_kiste.appendChild(table);
    }

}

function flascheTrinken(rowNumber, columnNumber) {
    console.log(`flasche trinken ${rowNumber} ${columnNumber}`);
    fetch(`/api/mate/trinken/${rowNumber}/${columnNumber}`, {
        method: 'POST',
    }).then(response => {
        if (response.status === 200) {
            console.log('flasche getrunken');
            let flasche = document.getElementById(`flasche-trinken-button-${rowNumber}-${columnNumber}`);
            flasche.disabled = true;
            flasche.style.backgroundColor = '#333';
        } else {
            alert('Fehler beim Trinken');
        }
    });
}
