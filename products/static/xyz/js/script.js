var mybutton = document.getElementById("myBtn");
var navBar = document.getElementById("headNav");
var x = navBar.style.backgroundColor;
var menu = document.getElementById("hello");
var padding;
var navh;
var x3 = document.getElementById("dummy");
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

//loader screen timout
// setTimeout(() => {
//   const box = document.getElementById('loader');
//   box.style.display = 'none';
// }, 6000);
var array = document.getElementsByClassName('flyerImg')

function initialize(){    
    for(i=0;i<array.length;i++){
        array[i].style.display = 'none';
    }
    array[current].style.display = 'block';
    menu.className = "navbar-collapse collapse"; 
    var w = window.innerWidth;
    ans = array[current].clientHeight;
    console.log(ans);
    navh = navBar.clientHeight;
    ans+=navh;
    // ans-=100;
    x3.style.position = 'relative';
    x3.style.top = navh+"px";
    h = window.innerHeight;
    document.getElementById("flyer").style.paddingTop = navh+"px";
    document.getElementById("flyer").style.overflow = "scroll";
    lefarr = document.getElementById("lefarr");
    main = document.getElementsByTagName("main")[0];
    main.style.position = 'relative';
    main.style.top = navh+"px";
    rigarr = document.getElementById("rigarr");
    lefarr.style.position = 'absolute';
    lefarr.style.top = h/2+'px';
    rigarr.style.top = h/2+'px';
    document.getElementById('flyer-nav').style.top = h+ 'px';
    // rigarr.style.right = ans/2+'px';
    if(w<992){
        console.log("hello")
        console.log(h)
    lefarr.style.top = ans/2+'px';
    rigarr.style.top = ans/2+'px';
    document.getElementById('flyer-nav').style.top = ans + 'px';
        for(i=0;i<array.length;i++){
            array[i].style.height = '';
        }
        padding = Math.ceil(ans*0.3);
        navBar.style.backgroundColor = "black";
        // x3.style.height = (ans+navh)+"px";
        block = 1;
        // document.getElementById("indent").style.display = "none";
    }
    else{
        for(i=0;i<array.length;i++){
            array[i].style.height = h-navh + 'px';
        }

        padding = Math.ceil(ans*0.45);
        block =0;
        // document.getElementById("indent").style.display = "block";
    }
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



  var intervalId = window.setInterval(function(){Left();}, 3000);
function Left(){
    array[current].className = 'flyerImg 1 flyer-left-invisible';
    temp = current;
    current = (current-1);
    if(current<0){
        current = 5;
    }
    console.log("LEFT INITIALTED")
    array[current].className = 'flyerImg 1 flyer-left';
    // array[current].style.display = 'block';
    array[temp].style.display = 'none';
    array[current].style.display = 'block';
}

function Right(){
    array[current].className = 'flyerImg 1 flyer-right-invisible';
    temp = current;
    current = (current+1)%6;
    
    console.log("LEFT INITIALTED")
    array[current].className = 'flyerImg 1 flyer-right';
    // array[current].style.display = 'block';
    array[temp].style.display = 'none';
    array[current].style.display = 'block';
}

