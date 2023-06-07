#!/usr/bin/node
const passingValue = parseInt(process.argv[2]);
if (!isNaN(passingValue)) {
  console.log(`My number: ${passingValue}`);
} else {
  console.log('Not a number');
}
