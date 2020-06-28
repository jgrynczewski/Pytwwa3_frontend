let counter = 0

document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('button').onclick = function () {
        counter++;
        document.querySelector('h1').innerHTML = counter;

        if (counter % 10 == 0) {
            alert(`Wartość licznika wynosi ${counter}`);
        }
    };
});