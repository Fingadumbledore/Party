function getMateStatus(socket) {
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
            if (!flascheIstVoll) { 
                rows[x].appendChild(cell);
                continue;
            }
            cell.classList.add('flasche');
            cell.classList.add(x);
            cell.classList.add(y);
            cell.classList.add(`voll-${flascheIstVoll}`);

            const flascheTrinkenButton = document.createElement('button');
            flascheTrinkenButton.classList.add('flasche-trinken-button');
            flascheTrinkenButton.style.backgroundColor = '#c88a35';
            flascheTrinkenButton.id = `flasche-trinken-button-${x}-${y}`; //TODO: remove and replace with class
            flascheTrinkenButton.onclick = () => { flascheTrinken(x, y) };
            cell.appendChild(flascheTrinkenButton);

            if (rows[x]) rows[x].appendChild(cell);
        }

        rows.forEach(row => table.appendChild(row));

        mate_kiste.appendChild(table);
    });
}

// returns x and y
function flascheIndex(index_1d, rows, columns) {
    return [Math.floor(index_1d / columns), index_1d % columns];
}

//TODO: replace id lookup with class lookup
function flascheTrinken(rowNumber, columnNumber) {
    console.log(`flasche trinken ${rowNumber} ${columnNumber}`);
    socket.emit('mate-nehmen', { 'row': rowNumber, 'column': columnNumber }, (data) => {
        console.log('flasche getrunken');
        let flasche = document.getElementById(`flasche-trinken-button-${rowNumber}-${columnNumber}`);
        flasche.disabled = true;
        flasche.style.backgroundColor = '#333';
    });
}

socket.on('mate-genommen', (data) => {
    console.log(data)
});
