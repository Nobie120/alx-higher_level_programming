#!/usr/bin/node

const factorize = (n) => {
  if (isNaN(n)i || n === 0) {
    return 1;
  }
  if (n < 0) {
    return -1;
  } else {
    return n * factorize(n - 1);
  }
};

const n = parseInt(process.argv[2]);
console.log(n);
