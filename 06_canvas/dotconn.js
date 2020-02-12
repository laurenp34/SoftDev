function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    prevX = -1;
    prevY = -1; //reset prevX,Y
}

var canvas, ctx;
var prevX= -1; //not in canvas yet (no prev)
var prevY= -1;
var curX, curY;

function setup() {
    canvas = document.getElementById('playground');
    ctx = canvas.getContext("2d");

    ctx.strokeStyle = "#964B00";
    ctx.fillStyle = "#964B00";
    ctx.lineWidth = 10;
    //check if mouse is clicked:
    canvas.addEventListener("mousedown", function (e) {
      console.log("mousedown");
      curX = e.clientX - canvas.offsetLeft;
      curY = e.clientY - canvas.offsetTop;
				//ctx.fillRect(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop, 3,3)
				ctx.beginPath(); //begins a path (to draw arc for circle) based on where the user's mouse is
				//draw circumference of circle
				ctx.arc(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop, 10, 0, 2 * Math.PI);
				ctx.stroke();
				// ctx.fillStyle = "#f49561";
				ctx.fill(); //fill in circle shape

        //if prevx,y defined, draw line to it
        if (prevX != -1 && prevY != -1) {
          ctx.moveTo(curX,curY);//reset start of segment to be center of dot
          ctx.lineTo(prevX,prevY);
          ctx.stroke();
        }

        prevX = e.clientX - canvas.offsetLeft;
        prevY = e.clientY - canvas.offsetTop;

    }, false);
}
