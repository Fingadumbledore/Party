
// zum prüfen ob Benutzer eingelogt ist
var s = sessionStorage.getItem("sessionID")
if (s == null) {
window.location.replace("http://127.0.0.1:5000/passwd")
}

// Magie um die Tabs anzuzeigen
function change_div(pfad)
{
        for (var i = 0; i < document.getElementsByClassName("tmplt_tab").length; i++) document.getElementsByClassName("tmplt_tab")[i].hidden = true;
        console.log(pfad)
        document.getElementById(pfad).hidden = false;
}
// Magie um die Tabs anzuzeigen
function change_game(pfad)
{
        for (var i = 0; i < document.getElementsByClassName("tmplt_tab1").length; i++) document.getElementsByClassName("tmplt_tab1")[i].hidden = true;
        console.log(pfad)
        document.getElementById(pfad).hidden = false;
}

// Benutzer anzeigen unter session
let name = sessionStorage.getItem("name");
document.getElementById("user").innerHTML = name;	







