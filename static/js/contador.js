var dv = document.getElementById("content");
dv.style.opacity = 1;
var val = 0;

function timer() {
    var start = new Date(2023, 10, 2, 16, 0);
    var t = start - new Date();
    var d = Math.floor(t / 1000 / 60 / 60 / 24);
    var h = Math.floor(t / 1000 / 60 / 60 % 24);
    if (h < 10) {
        h = "0" + h;
    }
    var m = Math.floor(t / 1000 / 60 % 60);
    if (m < 10) {
        m = "0" + m;
    }
    var s = Math.floor(t / 1000 % 60);
    if (s < 10) {
        s = "0" + s;
    }
    try {
        document.getElementById("d").innerHTML = d;
        document.getElementById("h").innerHTML = h;
        document.getElementById("m").innerHTML = m;
        document.getElementById("s").innerHTML = s;
    }
    catch (e){

    }
    try {
        document.getElementById("d1").innerHTML = d;
        document.getElementById("h1").innerHTML = h;
        document.getElementById("m1").innerHTML = m;
        document.getElementById("s1").innerHTML = s;
    }
    catch (e){

    }
    try {
        document.getElementById("d2").innerHTML = d;
        document.getElementById("h2").innerHTML = h;
        document.getElementById("m2").innerHTML = m;
        document.getElementById("s2").innerHTML = s;
    }
    catch (e){

    }
}

function fadein() {
    if (val < 1) {
        val += 0.025;
        dv.style.opacity = val;
    } else {
        clearInterval(fadeinInterval);
        if (ok == 2) {
            ok += 1;
        }
    }
}

var fadeInterval;
var fadeinInterval;

timer();
setInterval(timer, 1000);
