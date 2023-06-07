#!/usr/bin/node
function checkingArgument (argument) {
  if (argument) {
    console.log('Argument found');
  } else {
    console.log('No argument');
  }
}
const passingParameter = process.argv[2];
checkingArgument(passingParameter);
