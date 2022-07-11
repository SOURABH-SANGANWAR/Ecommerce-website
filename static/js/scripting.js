var navBar = document.getElementById("headNav");

navh = navBar.clientHeight;

document.getElementById('dummy-nav').style.height = navh+'px';
var a = document.getElementById('About');
var b = document.getElementById('Buy');
var c = document.getElementById('Reviews');

function ShowBlock(id){
    a.style.display = 'none';
    b.style.display = 'none';
    c.style.display = 'none';
    document.getElementById(id).style.display = 'block';
}