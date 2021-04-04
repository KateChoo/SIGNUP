const nav = document.getElementById('nav');
const p = document.getElementsByTagName('p')[0];
const s1 = document.querySelector('.s1');
const s2 = document.querySelector('.s2');
const s3 = document.querySelector('.s3');
//const span = document.querySelectorAll('#nav span');
const showLi = document.querySelectorAll('.show');

nav.addEventListener('click', toggle)
let navToggle = false;

function open(){
  s1.style.transform = "rotate(45deg) translateX(13px) translateY(5px)";
  s2.style.backgroundColor = "transparent";
  s3.style.transform = "rotate(-45deg) translateX(13px) translateY(-5px)";
  var i;
  for (i = 0; i < showLi.length; i++) {
    showLi[i].style.display = "block";
    //showLi[i].style.transform = "translateX(-13px) translateY(5px)";
    showLi[i].style.position = "relative";
  }
  navToggle = true;
}

function close(){
  s1.style.transform = "rotate(0deg) translateX(0px) translateY(0px)";
  s2.style.backgroundColor = "rgb(90, 90, 90)";
  s3.style.transform = "rotate(0deg) translateX(0px) translateY(0px)";
  var i;
  for (i = 0; i < showLi.length; i++) {
    showLi[i].style.display = "none";
  }
  navToggle = false;
}

function toggle(){
  navToggle ? close() : open();
}


