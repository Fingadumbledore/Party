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
            socket.emit('chat-get-messages', { count: 100, skip: 0 }, (data) => {
                sessionStorage['alreadyLoadedMessages'] += 100;
                let message_array = [];
                // dont fucking touch this
                data = JSON.parse(data.data.messages)

                for (let message of data) {
                    message_array.push(chatMessage(message.content, message.author, message.timestamp));
                }

                const chatBox = document.getElementById('chatBox');
                message_array.forEach(message => chatBox.appendChild(message));

                chatBox.style.overflow = 'auto';
                chatBox.scrollTop = chatBox.scrollHeight;
            });
            break;
        case 6: // Mate
            socket.emit('mate-status', (data) => {
                let flaschen = data.data;

                console.log(flaschen)
                const ROWS = 4;
                const COLUMNS = 5;

                var mate_kiste = document.getElementById('mate_kiste');
                var table = document.createElement('tbody');

                let rows = [];

                for (let rowNumber = 0; rowNumber < ROWS; rowNumber++) {
                    const row = document.createElement('tr');
                    rows.push(row);
                }

                for (let a = 0; a < flaschen.length; a++) {
                    const [x, y] = flascheIndex(a, ROWS, COLUMNS);
                    const flascheIstVoll = flaschen[a];

                    const cell = document.createElement('td');
                    cell.classList = ['flasche', x, y, `voll-${flascheIstVoll}`];

                    const flascheTrinkenButton = document.createElement('button');
                    flascheTrinkenButton.classList.add('flasche-trinken-button');
                    flascheTrinkenButton.disabled = !flascheIstVoll;
                    if (!flascheIstVoll) flascheTrinkenButton.style.backgroundColor = 'red';
                    flascheTrinkenButton.style.backgroundColor = flascheIstVoll ? '#c88a35' : '#333';
                    flascheTrinkenButton.id = `flasche-trinken-button-${x}-${y}`; //TODO: remove and replace with class
                    flascheTrinkenButton.onclick = () => flascheTrinken(x, y);
                    cell.appendChild(flascheTrinkenButton);

                    rows[x].appendChild(cell);
                }

                rows.forEach(row => table.appendChild(row));

                mate_kiste.appendChild(table);
            });
    }
}

function chatMessage(content, author, timestap) {
    console.log(content, author, timestap);
    const message = document.createElement('div');
    message.classList.add('chat-message');

    const messageContent = document.createElement('div');
    messageContent.classList.add('chat-message-content');
    const content_field = document.createElement('p');
    content_field.textContent = content;
    messageContent.appendChild(content_field);

    const messageAuthor = document.createElement('div');
    messageAuthor.classList.add('chat-message-author');
    const author_field = document.createElement('p');
    author_field.textContent = author;
    messageAuthor.appendChild(author_field);

    const messageTimestamp = document.createElement('div');
    messageTimestamp.classList.add('chat-message-timestamp');
    const timestamp_field = document.createElement('p');
    timestamp_field.textContent = timestap;
    messageTimestamp.appendChild(timestamp_field);

    const messageDetails = document.createElement('div');
    messageDetails.classList.add('chat-message-details');
    messageDetails.appendChild(messageAuthor);
    messageDetails.appendChild(messageTimestamp);

    message.appendChild(messageDetails);
    message.appendChild(messageContent);

    return message;
}



// returns x and y
function flascheIndex(index_1d, rows, columns) {
    return [Math.floor(index_1d / columns), index_1d % columns];
}

//TODO: replace id lookup with class lookup
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

function sendData(endpoint) {
    fetch(endpoint, {
      method: 'POST',
      body: JSON.stringify(true)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Fehler beim Senden der Daten.');
        }
      })
      .catch(error => {
        alert(error.message);
      });
  }
