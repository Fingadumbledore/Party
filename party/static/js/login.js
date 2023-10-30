const isMobile = /Mobi|Android/i.test(navigator.userAgent);
const deviceData = {
    isMobile: isMobile,
    userAgent: navigator.userAgent
  };

  document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Verhindert das normale Absenden des Formulars
    
    var nameInput = document.getElementById("nameInput");
    var name = nameInput.value;
    
    sessionStorage.setItem("name", name);
    
    // Das Formular manuell absenden
    this.submit();
});