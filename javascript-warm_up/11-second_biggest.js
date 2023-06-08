#!/usr/bin/node
function findSecondLargestInteger (args) {
  if (args.length <= 1) {
    return 0;
  }
  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < args.length; i++) {
    const current = parseInt(args[i]);

    if (current > largest) {
      secondLargest = largest;
      largest = current;
    } else if (current > secondLargest && current !== largest) {
      secondLargest = current;
    }
  }

  return secondLargest;
}
const result = findSecondLargestInteger(process.argv.slice(2));
console.log(`${result}`);
