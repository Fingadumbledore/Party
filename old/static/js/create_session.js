const checkbox = document.getElementById('checkbox');
const numberInput = document.getElementById('number');
const createButton = document.getElementById('createButton');

checkbox.addEventListener('change', function() {
    numberInput.disabled = !checkbox.checked;
});

createButton.addEventListener('click', function() {
    const inputValue = document.getElementById('name').value;

    if (inputValue !== '') {
        window.location.href = '/session'; 
    } else {
        alert('Bitte füllen Sie das Input-Feld aus.'); 
    }
});
cancelButton.addEventListener('click', function() {
    window.location.href = '/';
});