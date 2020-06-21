function hello() {
    alert('Hello, world!');
}

document.addEventListener('DOMContentLoaded', function start() {
    document.querySelector("button").onclick = hello;
});