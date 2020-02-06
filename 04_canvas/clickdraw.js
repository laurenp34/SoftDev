
function makeRect() {
	ctx.fillRect( 50, 50, 100, 200);
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

var canvas, ctx,
	mousePoint = false,
    prevX = 0,
    currX = 0,
    prevY = 0,
    currY = 0
    ;
var mode = "";
var startX, startY = 0;
var mousedown = false;

function setup() {
    canvas = document.getElementById('slate');
    ctx = canvas.getContext("2d");
		mode = document.getElementById("mode").value;

    canvas.addEventListener("mousemove", function (e) {

				if (mode == "line") {
					ctx.fillstyle = "#5799EC";
					findxy('move', e);
				} else if (mode == "rect" && mousedown) {
					ctx.fillStyle = "#DFB3EA";
					console.log("making rect. start: "+startX+", "+startY);
					ctx.clearRect(startX, startY, prevX-startX, prevY-startY);
					prevX = e.clientX - canvas.offsetLeft;
					prevY = e.clientY - canvas.offsetTop;
					ctx.fillRect(startX, startY, prevX-startX, prevY-startY);
					console.log("width: " + (prevX-startX).toString())
				}
				console.log("move");
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        //findxy('down', e)
				mousedown = true;
				mode = document.getElementById("mode").value;

				if (mode == "dot") {
					ctx.fillStyle = "#FF0000";
					ctx.fillRect(e.clientX - canvas.offsetLeft, e.clientY - canvas.offsetTop, 3,3)
				} else if (mode == "rect"){
					startX = e.clientX - canvas.offsetLeft;
					prevX = e.clientX - canvas.offsetLeft;
					startY = e.clientY - canvas.offsetTop;
					prevY = e.clientY - canvas.offsetTop;
					console.log("start: "+ startX+", "+startY);
				} else {
					findxy('down', e);
				}
    }, false);
    canvas.addEventListener("mouseup", function (e) {
				mousedown = false;
        findxy('up', e)
				console.log("up");
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);
}

function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY); // start point of line
    ctx.lineTo(currX, currY); // draw line to current point
    // ctx.strokeStyle = 'black';
    ctx.lineWidth = 10;
    ctx.stroke();
    ctx.closePath();
}

function findxy(mouseMove, e) {
    if (mouseMove == 'down') {
        prevX = currX; // make new starting point at where mouse is down
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft; // mouse coordinate made current point
        currY = e.clientY - canvas.offsetTop;

        mousePoint = true;
    }
    if (mouseMove == 'up' || mouseMove == "out") {
        mousePoint = false;
    }
    if (mouseMove == 'move') {
        if (mousePoint) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            draw();
        }
    }
}
