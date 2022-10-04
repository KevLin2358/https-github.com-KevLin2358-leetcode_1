/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let conv = convert(s);
    let revConv = conv.split("").reverse().join("");
    
    if(conv === revConv) return true;
    else return false;
};

var convert = function(str){
    let alpha = "abcdefghijklmnopqrstuvwxyz0123456789";
    let string = "";
    let charas = str.toLowerCase().split("");
    for(let i = 0; i < charas.length; i++){
        if(alpha.includes(charas[i]))string+=charas[i]
    }
    return string;
}