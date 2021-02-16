/*
Possible topics to explore: 
  1.) Iterating over strings
  2.) Immutability
  3.) while loop example
  4.) (extra) let, const and var

*/
 

/*
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(n).
 * - Space: O(n).
 * @param {string} str String to be reversed.
 * @return {string} The given str reversed.
 */
function reverseString(str) {
  let reversedStr = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr+= str[i];
  }
  return reversedStr;
}

console.log(reverseString(str1), reverseString(str1) == expected1);
console.log(reverseString(str2), reverseString(str2) == expected2);

/*****************************************************************************/

