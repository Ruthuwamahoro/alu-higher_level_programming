#!/usr/bin/node

function incrementAndCall(number, theFunction) {
  number++;
  theFunction(number);
}

function myFunction(number) {
  console.log("Number:", number);
}

incrementAndCall(5, myFunction);
