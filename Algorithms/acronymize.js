/*****************************************************************************/

/* 
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @return {string} The given str converted into an acronym.
 */

// without using .split()
function acronymize(str) {

}

// Test cases
const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

const str3 = "              ";
const expected3 = "";

const str4 = "LivefromNewYork,it'sSaturdayNight!";
const expected4 = "L";

const str5 = "     there's     no free lunch -     gotta pay yer way.    ";
const expected5 = "TNFL-GPYW";


// Testing -- will print the return value and true if it worked.
console.log(acronymize(str1), acronymize(str1) == expected1); 
console.log(acronymize(str2), acronymize(str2) == expected2);
console.log(acronymize(str3), acronymize(str3) == expected3);
console.log(acronymize(str4), acronymize(str4) == expected4);
console.log(acronymize(str5), acronymize(str5) == expected1);
/*****************************************************************************/