var mybutton = document.getElementById("myBtn");
var navBar = document.getElementById("headNav");
var x = navBar.style.backgroundColor;
var menu = document.getElementById("collmenu");
var padding;
var navh;
// var x3 = document.getElementById("dummy");
var intro = document.getElementById("welco");
var block = 0;
// var topSellers = document.getElementsByClassName()
var dyn = document.getElementById("dynText");
var intext = "I am "
var list = ["a web devoloper", "an AI enthuisast", "a Backend Developer"] 
var current = 0
var ind = 0
var toggle = 0
var current = 0;
var searchBar = document.getElementById('searchBar')
//loader screen timout
// setTimeout(() => {
//   const box = document.getElementById('loader');
//   box.style.display = 'none';
// }, 6000);
function initialize(){    
    searchBar.style.display = 'none'
    menu.className = "navbar-collapse collapse"; 
    var w = window.innerWidth;
    ans = 0
    navh = navBar.clientHeight;
    searchBar.style.top = navh + 'px';
    ans+=navh;
    // ans-=100;
    h = window.innerHeight;
    // document.getElementById("flyer").style.paddingTop = navh+"px";
    // document.getElementById("flyer").style.overflow = "scroll";
    // lefarr = document.getElementById("lefarr");
    main = document.getElementsByTagName("main")[0];
    main.style.position = 'relative';
    main.style.top = navh+"px";
    rigarr = document.getElementById("rigarr");
    // scrollFunction();
}
initialize();
initialize();
initialize();

$(window).resize(function() {initialize();});

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    var scrolled = document.documentElement.scrollTop
    // var height = x3.clientHeight;
    // var map = 1-scrolled/height;
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
    } 
    else {
    mybutton.style.display = "none";
    }
    // if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    //     navBar.style.backgroundColor = "black";
    // } 
    // else {
    //     navBar.style.backgroundColor = x;
    // }
    // if(block==1){
    //     navBar.style.backgroundColor = "black";
    // }
}

function screenTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function hello(x){
    let depth =  document.getElementById(x).getBoundingClientRect().y;

    if(block==0){
        depth-=navh;
    }
    console.log(depth);
    document.getElementById("hello").className = "navbar-collapse collapse";
    document.documentElement.scrollTop += depth;
}


function DoAnimation() {
    var targetElement = document.getElementById("flyer");
    // if(targetElement.className =! "animate"){
    targetElement.className = "animate";
    navBar.className = "navbar navbar-expand-lg navbar-dark animated";
    // else
    // targetElement.className = "animated";
  }

  function HideAnimation() {
    var targetElement = document.getElementById("flyer");
    // if(targetElement.className =! "animate"){
    targetElement.className = "animated";
    navBar.className = "navbar navbar-expand-lg navbar-dark animate";
    // else
    // targetElement.className = "animated";
  }

