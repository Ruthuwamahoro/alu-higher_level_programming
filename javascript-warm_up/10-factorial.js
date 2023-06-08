#!/usr/bin/node
function factorial(number) {
  if (isNaN(number)) {
    return 1;
  } else if (number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const result = factorial(parseInt(process.argv[2]));
console.log(`${result}`);
