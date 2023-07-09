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