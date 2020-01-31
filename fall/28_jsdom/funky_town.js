// Lauren Pehlivanian
// SoftDev1 pd9
// K #28: Sequential Progression II: Electric Boogaloo
// 2019-12-11
//TEAM POSTFIX

/*
var foo = function(n){
  return n;
};
*/

var factorial = function(n){
  if (n == 1) return 1;
  return (n * factorial(n-1));
};


var fibonacci = function(n){
  if (n < 2) return n;
  if (n == 2) return 1;
  return (fibonacci(n-1) + fibonacci(n-2));
};

var gcd = function(a,b){
  if (a < b){
    return gcd(b, a);
  }
  if (a % b == 0) return b;
  return gcd(a-b, b);
};

students = ['Manfred', 'Biraj', 'Tammy', 'Fluffy', 'Unicorn']

var randomStudent = function(){
  var index = Math.floor(Math.random() * students.length);
  return students[index];
};

var text; //to store answer
var print_ans = false;

var forFactorial = document.getElementById("fact");
forFactorial.addEventListener('click', function(){
  console.log(factorial(17));
  text = factorial(17);
  var display = document.getElementById("ans");
  display.innerHTML = text + "<br>";
});


var forFib = document.getElementById("fib");
forFib.addEventListener('click', function(){
  console.log(fibonacci(19));
  text = fibonacci(19);
  var display = document.getElementById("ans");
  display.innerHTML = text + "<br>";
});

var forStudent = document.getElementById("name");
forStudent.addEventListener('click', function(){
  console.log(randomStudent());
  text = randomStudent();
  var display = document.getElementById("ans");
  display.innerHTML = text + "<br>";
  // var node = document.createTextNode(text);
  // display.appendChild(node);
  // document.write("<br>");
});

var forGcd = document.getElementById("gcd");
forGcd.addEventListener('click', function(){
  console.log(gcd(150,20));
  text = gcd(150,20);
  var display = document.getElementById("ans");
  display.innerHTML = text + "<br>";

});

// if (print_ans) {
//   document.write(text);
//   print_ans = false;
// };
