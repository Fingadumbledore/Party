/*window.onload = function() {
  const username = document.getElementById('userNameEntry').innerHTML;
  const ws = new WebSocket('ws://localhost:5000')
  ws.addEventListener('open', (e) => {
    ws.send(JSON.stringify({
      'user': 'test'
    }))
  })

  function join_chat() {
    ws.send(JSON.stringify({
      'msg_type': 'user_join',
      'username': username
    }))
  } 
}*/

let unread = 0;

function updateTitle() {
  document.title = "Chat (" + unread + ")";
}

function addMessage(username, message, timestamp) {
  let messagesDiv = document.getElementById("messages");
  let messageDiv = document.createElement("div");
  messageDiv.classList.add("message");
  let usernameSpan = document.createElement("span");
  usernameSpan.classList.add("username");
  usernameSpan.innerText = username;
  let messageSpan = document.createElement("span");
  messageSpan.innerText = message.substring(0, 80);
  let timestampSpan = document.createElement("span");
  timestampSpan.classList.add("timestamp");
  timestampSpan.innerText = timestamp;
  messageDiv.appendChild(usernameSpan);
  messageDiv.appendChild(document.createTextNode(": "));
  messageDiv.appendChild(messageSpan);
  messageDiv.appendChild(document.createElement("br"));
  messageDiv.appendChild(timestampSpan);
  messagesDiv.appendChild(messageDiv);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
  unread += 1;
  updateTitle();
}

let inputField = document.getElementById("input");
inputField.addEventListener("input", function() {
  let value = inputField.value;
  if (value.length > 80) {
    inputField.value = value.substring(0, 80);
  }
});

function getMessages() {
var xhr = new XMLHttpRequest();
xhr.open("GET", "/get");
xhr.onload = function() {
  document.getElementById("messages").innerHTML = xhr.responseText;
};
xhr.send();
}

function sendMessage() {
var message = document.getElementById("message").value;
var uname = sessionStorage.getItem("name")
document.getElementById('username').value = uname; 
var username = document.getElementById("username").value;

var xhr = new XMLHttpRequest();
xhr.open("POST", "/send");
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
xhr.send("message=" + message + "&username=" + username);
}
