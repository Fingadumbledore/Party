function setUID() {
    let sessID = document.getElementById("Uid").value
    window.sessionStorage.setItem("userID", sessID)
}

function setID1() {
    let sessID = document.getElementById("id1").value
    window.sessionStorage.setItem("sessionID", sessID)
}

function setID2() {
    let sessID = document.getElementById("id2").value
    window.sessionStorage.setItem("sessionID", sessID)
}

function setname2() {
    let sessID = document.getElementById("name2").value
    window.sessionStorage.setItem("name", sessID)
}

function setname3() {
    let sessID = document.getElementById("name3").value
    window.sessionStorage.setItem("name", sessID)
}

function randomnumber(min, max) { 
        rnumber =  Math.floor(Math.random() * (max - min + 1) ) + min
        document.getElementById("Uid1").innerHTML = rnumber	
        window.sessionStorage.setItem("userID", rnumber)
    }