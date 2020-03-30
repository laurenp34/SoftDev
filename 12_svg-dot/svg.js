// Kiran Vuksanaj and Lauren Pehlivanian
// Softdev2 pd9
// K12 - Connect the dots svg style
// 03-30-2020
console.log("connected svg.js");
// ELEMENT SELECTORS
var clearButton = document.getElementById("clear-button");
var vImage = document.getElementById("vimage");

var sampleDot = document.getElementById("sample-dot");
var sampleLine = document.getElementById("sample-line");

// GLOBAL VARIABLES
var prevX = -1;
var prevY = -1;

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
	e.preventDefault();
	console.log(e);
	console.log(prevX,prevY);
	// clone sample line and dot, change properties, then add them to the vimage
	let newDot = sampleDot.cloneNode();
	let newLine = sampleLine.cloneNode();

	newDot.setAttribute("cx",e.layerX);
	newDot.setAttribute("cy",e.layerY);
	newDot.removeAttribute("display");
	newDot.removeAttribute("id");
	vImage.appendChild(newDot);

	if(prevX != -1 && prevY != -1){
		newLine.setAttribute("x1",prevX);
		newLine.setAttribute("y1",prevY);
		newLine.setAttribute("x2",e.layerX);
		newLine.setAttribute("y2",e.layerY);
		newLine.removeAttribute("display");
		newLine.removeAttribute("id");
		vImage.appendChild(newLine);
	}
	prevX = e.layerX;
	prevY = e.layerY;
}



// EVENT LISTENERS
clearButton.addEventListener('click',clear);
vImage.addEventListener('click',addDot);
