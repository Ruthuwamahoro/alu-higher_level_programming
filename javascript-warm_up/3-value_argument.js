#!/usr/bin/node
function printingArgument (argument) {
  if (argument) {
    console.log(`${argument}`);
  } else {
    console.log('No argument');
  }
}
const passingArgument = process.argv[2];
printingArgument(passingArgument);
