
let moderator = document.getElementById('mod')
let select = document.getElementById('job')
let viewer = document.getElementById('viewer')
let form = document.getElementById('form')

let role;

moderator.addEventListener('click', () => {
    select.style.display = 'block';
});

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    if(viewer.checked){
        role = 'viewer'
    }else{
        role = 'moderator'
    }
})


// export function getRole() {
//     return role;
// }