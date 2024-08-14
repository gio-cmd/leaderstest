// import role from './register'
const role = 'administrator';

if (role === 'administrator') {
    const removeButtons = document.querySelectorAll('.remove-btn');
    for (let i = 0; i < removeButtons.length; i++) {
        removeButtons[i].onclick = function() {
            const row = this.parentNode.parentNode;
            row.parentNode.removeChild(row);
        };
    }

    const editButtons = document.querySelectorAll('.edit-btn');
    for (let i = 0; i < editButtons.length; i++) {
        editButtons[i].onclick = function() {
            const row = this.parentNode.parentNode;
            const cells = row.getElementsByTagName('td');
            
            if (this.innerHTML === 'Edit') {
                for (let j = 0; j < cells.length - 1; j++) {
                    const cellText = cells[j].innerHTML;
                    cells[j].innerHTML = `<input type="text" value="${cellText}">`;
                }
                this.innerHTML = 'Save';
            } else {
                for (let j = 0; j < cells.length - 1; j++) {
                    const input = cells[j].querySelector('input');
                    cells[j].innerHTML = input.value;
                }
                this.innerHTML = 'Edit';
            }
        };
    }
}