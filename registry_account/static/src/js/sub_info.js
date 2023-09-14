const myInput = document.getElementById('o8yer21ma2892');
const infoBubble = document.getElementById('infoBubble');
myInput.addEventListener('focus', () => {
    infoBubble.classList.add('active');
});
myInput.addEventListener('blur', () => {
    infoBubble.classList.remove('active');
});