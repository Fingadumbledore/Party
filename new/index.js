function updateEventsTable() {
    fetch('/api/planer')
        .then(function (response) { return response.json(); })
        .then(function (data) {
        var events = JSON.parse(data.events);
        var tableBody = document.querySelector('#events tbody');
        // macht die tabelle voll
        events.forEach(function (event) {
            var row = document.createElement('tr');
            var nameCell = document.createElement('td');
            var timeCell = document.createElement('td');
            var statusCell = document.createElement('td');
            var manageCell = document.createElement('td');
            nameCell.textContent = event.name;
            timeCell.textContent = event.time;
            statusCell.textContent = 'Wird wohl noch kommen';
            // Buttons zum bearbeiten eines events. Die bearbeitung muss aber noch gebaut werden
            var editButton = document.createElement('button');
            var deleteButton = document.createElement('button');
            editButton.classList.add('button-wrapper');
            deleteButton.classList.add('button-wrapper');
            editButton.innerHTML = '<img src="/static/icons/edit.png" alt="Edit">';
            deleteButton.innerHTML = '<img src="/static/icons/x.png" alt="Delete">';
            manageCell.appendChild(editButton);
            manageCell.appendChild(deleteButton);
            row.appendChild(nameCell);
            row.appendChild(timeCell);
            row.appendChild(statusCell);
            row.appendChild(manageCell);
            tableBody.appendChild(row);
        });
    })
        .catch(function (error) { return console.error('Error fetching events:', error); });
}
updateEventsTable();
