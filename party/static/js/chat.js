function getNChatMessages(socket, count, skip) {
            socket.emit('chat-get-messages', { count: 170, skip: 0 }, (data) => {
                sessionStorage['alreadyLoadedMessages'] += 100;
                let message_array = [];
                // dont fucking touch this
                data = JSON.parse(data.data.messages)

                for (let message of data) {
                    console.log(message)
                    message_array.push(buildChatMessage(message.sender, message.text, message.timestamp));
                }

                const chatBox = document.getElementById('chatBox');
                message_array.forEach(message => chatBox.appendChild(message))

                chatBox.scrollTop = chatBox.scrollHeight;
            });
}

function buildChatMessage(author, content, timestamp) {
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
    timestamp_field.textContent = timestamp;
    messageTimestamp.appendChild(timestamp_field);

    const messageDetails = document.createElement('div');
    messageDetails.classList.add('chat-message-details');
    messageDetails.appendChild(messageAuthor);
    messageDetails.appendChild(messageTimestamp);

    message.appendChild(messageDetails);
    message.appendChild(messageContent);

    return message;
}

function sendMessage() {
    const chatInput = document.getElementById('chatInputField');
    if (chatInput.value.length < 0) return;

    let userName = window.sessionStorage.getItem('name');
    if (!userName) {
        userName = 'Peter';
    }

    const dt = new Date();
    const padL = (nr, len = 2, chr = `0`) => `${nr}`.padStart(2, chr);

    const dateStr = `${ dt.getFullYear()}-${ padL(dt.getMonth()+1)}-${ padL(dt.getDate())} ${ padL(dt.getHours())}:${ padL(dt.getMinutes())}:${ padL(dt.getSeconds())}`; // magic date formatter

    const message = { sender: userName, text: chatInput.value, timestamp: dateStr };

    console.log(message);

    socket.emit('chat-message', message);
    console.log('message sent');

    chatInput.value = '';
}

socket.on('chat-message', (data) => {
    const chatBox = document.getElementById('chatBox');
    console.log(data);
    // check if sender is given
    let message = buildChatMessage(data.sender, data.text, data.timestamp); // $date is mongodb date
    console.log(data.timestamp);
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
});


window.addEventListener('load', () => {
    getNChatMessages(socket, 100, 0);
});
