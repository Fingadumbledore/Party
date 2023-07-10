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
