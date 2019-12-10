var fact = function(n) {
        if (n == 1) {
                return n;
        }
        return n * fact(n-1);
};

var fibonacci = function(n) {
        if (n == 0) {
                return 0;
        }
        if (n == 1) {
                return 1;
        }
        return fibonacci(n-1) + fibonacci(n-2);

};

var gcd = function(a,b) {
        if (b > a) return gcd(b,a);
        else if (a % b == 0) return b;
        else return gcd(b, a%b);

};
