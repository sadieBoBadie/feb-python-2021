/* Jonathan Leon and group */

const str1 = " there's no free lunch - gotta pay yer way. l";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

const str3 = "              ";
const expected3 = "";

const str4 = "LivefromNewYork,it'sSaturdayNight!";
const expected4 = "L";

const str5 = "     there's     no free lunch -     gotta pay yer way.    ";
const expected5 = "TNFL-GPYW";
var someString = " Doge Coin to the Moon"

function acronymize(str) {
    var newString = "";
    if (str[0] != " "){
        newString += str[0].toUpperCase();
    }
    for(var i = 0; i < str.length-1; i++){
        if (str[i] == " " && str[i+1] != " "){
            newString += str[i+1];
        }
    }
    
    return newString.toUpperCase();

}
console.log(acronymize(str1))