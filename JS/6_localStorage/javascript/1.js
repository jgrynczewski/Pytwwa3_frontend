if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

document.addEventListener('DOMContentLoaded', function() {
    counter = localStorage.getItem('counter')
    document.querySelector('h1').innerHTML = counter;

    document.querySelector('button').onclick = function() {
        counter++;
        document.querySelector('h1').innerHTML = counter;
        localStorage.setItem('counter', counter);
    }
})