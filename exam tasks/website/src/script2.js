// import role from './register'
const role = 'administrator';

if (role === 'administrator') {
    document.querySelectorAll('.remove-btn').forEach(button =>
        button.addEventListener('click', () => button.closest('tr').remove())
    );

    document.querySelectorAll('.edit-btn').forEach(button =>
        button.addEventListener('click', editSave)
    );
}

function editSave() {
    const row = this.closest('tr');
    const cells = row.querySelectorAll('td:not(.actions)');
    const isEditing = this.classList.contains('edit-btn');

    cells.forEach(cell => {
        if (isEditing) {
            const input = document.createElement('input');
            input.value = cell.textContent;
            cell.textContent = '';
            cell.appendChild(input);
        } else {
            const input = cell.querySelector('input');
            cell.textContent = input ? input.value : '';
        }
    });

    this.textContent = isEditing ? 'Save' : 'Edit';
    this.classList.toggle('edit-btn');
    this.classList.toggle('save-btn');
}
