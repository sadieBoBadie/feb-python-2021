// Recursion:

/* When a function calls itself. */

// Non-recursive sigma (sum to num)
function sumToNum(num) {

    var count = 0

    for(var i = 1; i <= num; i++){
        count+= i
    }
    return count;
}

console.log(sumToNum(5)); // 1+2+3+4+5 ===> 15

// Recursive sigma
function sumToNum(num) {

    // Base case ---> stop condition
    if (num == 1) {
        return 1
    }
    // recursive call -- 
    // something has to change when you call the function
    // (increment or decrement)
    return sumToNum(num - 1) + num
}



console.log(sumToNum(3))