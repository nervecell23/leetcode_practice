var romanToInt = function(s) {
    var sArray = s.split("").reverse();
    var result = 0;
    var prevElement = 0;
    var romanHash = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };

    sArray.forEach(
        function(element){
            if(romanHash[element] < romanHash[prevElement]){
                result -= romanHash[element];
            }
            else{
                result += romanHash[element];
            }

            prevElement = element;
        });

    return result;

};
