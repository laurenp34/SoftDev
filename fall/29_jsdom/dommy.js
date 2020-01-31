// Calvin Chu
// SoftDev1 pd9
// K29 -- Sequential Progression III: Season of the Witch
// 2019-12-12

// Gets button element and calls addItem on click
var button = document.getElementById("b");
button.addEventListener('click', function(e){addItem(e)});

// Gets list element, creates a new li and appends it to the list, then sets appropriate EventListeners to new child
var addItem = function(e) {
  var list = document.getElementById("thelist");
  var item = document.createElement("li");
  item.innerHTML = "WORD";
  list.appendChild(item);
  item.addEventListener('mouseover', function(e){changeHeading(this.innerText)});
  item.addEventListener('mouseout', function(e){changeHeading("Hello World!")});
  item.addEventListener('click', function(e){removeItem(this); changeHeading("Hello World!");});
};

// Changes the heading of the page
var changeHeading = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = e;
};

// Removes the element that calls it
var removeItem = function(e) {
  e.remove();
};

// Gets the initial list and adds the appropriate EventListeners to them
var lis = document.getElementsByTagName("li");
for (var i = 0; i < lis.length; i++) {
  lis[i].addEventListener('mouseover', function(e){changeHeading(this.innerText)});
  //lis[i].addEventListener('mouseover', function(e){console.log(e.target)});
  lis[i].addEventListener('mouseout', function(e){changeHeading("Hello World!")});
  lis[i].addEventListener('click', function(e){removeItem(this); changeHeading("Hello World!");});
}

// Basic fib algorithm
var count = 0;
var fib = function(n) {
  if (n == 0) return 0;
  else if (n < 2) return 1;
  else return fib(n-1) + fib(n-2);
};

// Gets the fiblist, creates a new list element containing the next fib number (using the fib function) and appends it
var addFib = function(e) {
  console.log(e);
  console.log(fib(count));
  var list = document.getElementById("fiblist");
  var item = document.createElement("li");
  item.innerHTML = fib(count);
  list.appendChild(item);
  count++;
};
// Gets the fiblist, creates a new list element containing the next fib number (getting and using the last two numbers generated) and appends it
var addFib2 = function(e) {
  if (count < 3) return addFib(e);
  var list = document.getElementById("fiblist");
  var nums = list.childNodes;
  var item = document.createElement("li");
  var sum = parseInt(nums[nums.length - 1].textContent) + parseInt(nums[nums.length - 2].textContent);
  console.log(e);
  console.log(sum);
  item.innerHTML = sum;
  list.appendChild(item);
  count++;
};

// Gets fib button and calls addFib2 on click
var fb = document.getElementById("fb");
//fb.addEventListener('click', function(e){addFib(e)});
fb.addEventListener('click', function(e){addFib2(e)});
// button.addEventListener('click', function(e) {console.log(e);});
