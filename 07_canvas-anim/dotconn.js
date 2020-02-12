function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    prevX = -1;
    prevY = -1; //reset prevX,Y
}

function animaniate(e) {
		//e.preventDefault();
		animate = true;
				
}

function paintSlide(timestamp) {
	if (animate) {
		ctx.beginPath(); //begins a path (to draw arc for circle) based on where the user's mouse is
		//draw circumference of circle
		ctx.arc(300,300, radius, 0, 2 * Math.PI);
		ctx.stroke();
		ctx.fill(); //fill in circle shape
		if (expand) radius += 5;
		else radius -= .1;
		if (radius >= 300) expand = false;
		if (radius <= .5) expand = true;
	}
		
		window.requestAnimationFrame(paintSlide);		
}

var canvas, ctx, window, id;
var prevX= -1; //not in canvas yet (no prev)
var prevY= -1;
var animate = false;
var radius = 0.5;
var expand = true;

function setup() {
    canvas = document.getElementById('playground');
    ctx = canvas.getContext("2d");
    
    window = document.defaultView;
    id = window.requestAnimationFrame(paintSlide);
}
