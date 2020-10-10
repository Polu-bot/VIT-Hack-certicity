var x = document.getElementById("login");
var y = document.getElementById("register");
var l = document.getElementById("toggle-btn-l")
var r = document.getElementById("toggle-btn-r");
var lt = document.getElementById("l-text");
var rt = document.getElementById("s-text");

function register() {
    x.style.left = "-400px";
    y.style.left = "50px";
    l.style.display = "block";
    r.style.display = "none";
    lt.style.display = "block";
    rt.style.display = "none";
}

function login() {
    x.style.left = "50px";
    y.style.left = "450px";
    l.style.display = "none";
    r.style.display = "";
    lt.style.display = "none";
    rt.style.display = "";
}