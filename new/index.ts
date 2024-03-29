function updateEventsTable() {
    fetch('/api/planer')
        .then(response => response.json())
        .then(data => {
            const events = JSON.parse(data.events);
            const tableBody = document.querySelector<HTMLTableSectionElement>('#events tbody');

            // macht die tabelle voll
            events.forEach((event: { name: string; time: string }) => {
                const row = document.createElement('tr');
                const nameCell = document.createElement('td');
                const timeCell = document.createElement('td');
                const statusCell = document.createElement('td');
                const manageCell = document.createElement('td');

                nameCell.textContent = event.name;
                timeCell.textContent = event.time;
                statusCell.textContent = 'Wird wohl noch kommen';

                // Buttons zum bearbeiten eines events. Die bearbeitung muss aber noch gebaut werden
                const editButton = document.createElement('button');
                const deleteButton = document.createElement('button');

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
        .catch(error => console.error('Error fetching events:', error));
}

updateEventsTable();
