#!/usr/bin/node
function add(a=3,b=5){
	const sum = a+b;
	return sum;
}
const a = 10;
const b = 7;
const answer = add(a, b);
console.log(`${answer}`);

