function animaniate(e) {
    console.log(e);
		//e.preventDefault();
    //only create new animation frame if animation stopped
    //otherwise, animation would keep speeding up if already animating.
    mode = "anim"
}

function stop() {
   mode = "stop";
}

function dvd() {
	if( mode != "dvd"){
		mode = "dvd"
		logo_x = 15;
		logo_y = 15;
		logo_vx = 6;
		logo_vy = 4;
	}
}

function paintSlide(timestamp) {
	if (mode == "anim") {
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
	}else if (mode == "dvd") {
		ctx.clearRect(0,0,600,600);
		logo_x += logo_vx;
		logo_y += logo_vy;
		if(logo_x <= 0 || logo_x >= 600){
			logo_vx *= -1;
		}
		if(logo_y <= 0 || logo_y >= 600){
			logo_vy *= -1;
		}
		ctx.drawImage(logo,logo_x,logo_y,20,20);
	}

		id = window.requestAnimationFrame(paintSlide);
}

var canvas, ctx, window, id;
var mode = "stop";
var radius = 0.5;
var expand = true;
var logo, logo_x, logo_y,logo_vx,logo_vy; // the same vibe as netlogo, the x and y coordinates + the distance they should move in each direction with each new 'tick'

function setup() {
    canvas = document.getElementById('playground');
    ctx = canvas.getContext("2d");
    ctx.fillStyle = "#5799EC";

    window = document.defaultView;
    id = window.requestAnimationFrame(paintSlide);
    
    logo = new Image();
    logo.src = "pingu.jpg"
}

