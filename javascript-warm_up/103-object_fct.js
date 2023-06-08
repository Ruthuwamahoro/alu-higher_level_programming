#!/usr/bin/node
let myNumber = 5;

const incr = () => {
  myNumber++;
};

const incrementAndCall = (number, theFunction) => {
  theFunction(number);
};

const myFunction = (number) => {
  console.log('Number:', number);
};

incr();
incrementAndCall(myNumber, myFunction);
