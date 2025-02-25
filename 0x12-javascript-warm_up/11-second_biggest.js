#!/usr/bin/node

const list = process.argv.slice(2).map(Number);

if (list.length < 2) {
	console.log(0);
	return;
}
const sorted = list.sort((a, b) => a - b);
console.log(sorted[1]);
