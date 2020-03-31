// Kiran Vuksanaj and Lauren Pehlivanian
// Softdev2 pd9
// K12 - Connect the dots svg style
// 03-30-2020
console.log("connected svg.js");
// ELEMENT SELECTORS
var clearButton = document.getElementById("clear-button");
var vImage = document.getElementById("vimage");

var sampleDot = document.getElementById("sample-dot");

// GLOBAL VARIABLES
var prevX = -1;
var prevY = -1;
var dot = 0;

// FUNCTIONS
var clear = function(e) {
	// in following with example from DOM MDN - removeChild()
	while ( vImage.firstChild ) {
		vImage.removeChild( vImage.firstChild );
	}
	prevX = -1;
	prevY = -1;
	console.log("children of vImage removed")
}

var addDot = function(e) {
	//console.log(e.target);
	if (e.target.id == "vimage") {
		console.log("add");
		e.preventDefault();
		console.log(e);
		// console.log(prevX,prevY);
		// clone sample line and dot, change properties, then add them to the vimage
		let newDot = sampleDot.cloneNode();
		//let newLine = sampleLine.cloneNode();

		newDot.setAttribute("cx",e.layerX);
		newDot.setAttribute("cy",e.layerY);
		newDot.removeAttribute("display");
		newDot.removeAttribute("id");
		vImage.appendChild(newDot);

		//add listener for each new dot that is created
		newDot.addEventListener('click', clickDot);

		prevX = e.layerX;
		prevY = e.layerY;
	}
}

var clickDot = function(e) {
	dot = e.target; //get the dot that was clicked

	//if color is dark blue, change to aqua
	if (dot.getAttribute("fill") != "Aqua"){
		console.log("blue")
		e.target.setAttribute("fill", "Aqua");
	//if color alr aqua, move it to random cx and cy in frame (500x500)
	} else {
		console.log("hi")
		e.target.setAttribute("cx", Math.floor(Math.random() * 500));
		e.target.setAttribute("cy", Math.floor(Math.random() * 500));
	}
}


// EVENT LISTENERS
clearButton.addEventListener('click',clear);
dot = vImage.addEventListener('click',addDot);
