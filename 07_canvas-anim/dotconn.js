function animaniate(e) {
    console.log(e);
		//e.preventDefault();
    //only create new animation frame if animation stopped
    //otherwise, animation would keep speeding up if already animating.
    if (!animate) {
		    animate = true;
        id = window.requestAnimationFrame(paintSlide);
    }
}

function stop() {
  if (animate) {
    animate = false;
    window.cancelAnimationFrame(id);
  }
}

function paintSlide(timestamp) {
	if (animate) {
    ctx.clearRect(0,0,600,600);
		ctx.beginPath(); //begins a path (to draw arc for circle) based on where the user's mouse is
		//draw circumference of circle
		ctx.arc(300,300, radius, 0, 2 * Math.PI);
    console.log("drew circle radius "+radius);
		ctx.stroke();
		ctx.fill(); //fill in circle shape
		if (expand) radius += 2;
		else radius -= 2;
		if (radius >= 300) {
      ctx.strokeStyle = "#FF0000";
      expand = false;
    }
		if (radius <= .5) {
      ctx.fillStyle = "#5799EC";
      expand = true;
    }
	}

		id = window.requestAnimationFrame(paintSlide);
}

var canvas, ctx, window, id;
var animate = false;
var radius = 0.5;
var expand = true;

function setup() {
    canvas = document.getElementById('playground');
    ctx = canvas.getContext("2d");
    ctx.fillStyle = "#5799EC";

    window = document.defaultView;
    id = window.requestAnimationFrame(paintSlide);
}
