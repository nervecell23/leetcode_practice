function RomanToIntegerTest(){
  const RomanToInteger = require("./romanToInteger.js");
  var subject = new RomanToInteger();
  var testCase = [
    "MMM",
    "DCC",
    "XX",
    "IV"
  ];
  var expectedResult = [
    3000,
    700,
    20,
    4
  ];
  var testResult = testCase.map(element => subject.proceed(element));
  var counter = 0;

  console.log("test result : expected result");

  for(var i=0; i<testCase.length; i++){
    if(testResult[i] == expectedResult[i]) counter++;
    console.log(`${testResult[i]} : ${expectedResult[i]}`);
  }

  if(counter == testCase.length) console.log("PASS");
  else console.log("FAIL");
}

RomanToIntegerTest();
