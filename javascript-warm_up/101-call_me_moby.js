#!/usr/bin/node

function executeXTimes(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

function myFunction() {
  console.log("Executing the function");
}

executeXTimes(5, myFunction);
