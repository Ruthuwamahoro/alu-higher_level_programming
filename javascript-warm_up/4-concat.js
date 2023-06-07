#!/usr/bin/node
function printingArgument (argument1, argument2 = 0) {
  if (argument1 && argument2) {
    console.log(`${argument1} is ${argument2}`);
  } else if (argument1) {
    console.log(`${argument1} is undefined`);
  } else {
    console.log('undefined is undefined');
  }
}
const passingArgument1 = process.argv[2];
const passingArgument2 = process.argv[3];
printingArgument(passingArgument1, passingArgument2);
