let red;
let green;
let blue;
let rgbColor;

const randomColor = ()=> {
  for (var i = 0; i <=10; i += 1) {
  red = Math.floor(Math.random() * 256 );
  green = Math.floor(Math.random() * 256 );
  blue = Math.floor(Math.random() * 256 );
  rgbColor = 'rgb(' + red + ',' + green + ',' + blue + ')';
  // html += '<div style="background-color:' + rgbColor + '"></div>';
  return rgbColor;
  }
}

//const github = document.getElementById('github'); //icons[4]
github.addEventListener ('mouseover', () => {
github.style.color = randomColor();
});