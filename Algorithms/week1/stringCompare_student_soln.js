/* case insensitive string compare: Still O(n), but faster in best case scenarios */
function caseInsensitiveStringCompare(strA, strB) {
    if (strA.length != strB.length){
        return false;
    }
    for (var i = 0; i < strA.length; i++){
        if (strA[i].toLowerCase() != strB[i].toLowerCase()){
            return false;
        }
    }
    return true;
}