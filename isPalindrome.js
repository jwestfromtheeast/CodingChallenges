//LeetCode question 9. Palindrome Number
var isPalindrome = function(x) {
    for(var i = 0; i < x.toString().length / 2; i++) {
        if(x.toString().charAt(i) != x.toString().charAt(x.toString().length - 1 - i)) {
            return false;
        }
    }
    return true;
};

var isPalindrome2 = function(x) {   
    if(x < 0 || (x != 0 && x % 10 == 0)) { 
        return false; 
    }
    
    var revertedNumber = 0;
    while(x > revertedNumber) {
        revertedNumber = revertedNumber * 10 + x % 10;
        x = Math.floor(x / 10);
        console.log('here');
    }
    
    return (x == revertedNumber) || (x == Math.floor(revertedNumber / 10));
};

console.log(isPalindrome2(121));