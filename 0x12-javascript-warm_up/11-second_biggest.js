#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort((a, b) => b - a);
  console.log(second[1]);
}
