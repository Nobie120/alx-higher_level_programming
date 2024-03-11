#!/usr/bin/node

const factorize = (n) => {
  if (isNaN(n)) {
    return 1;
  }
  if (n <= 1) {
    return 1;
  } else {
    return n * factorize(n - 1);
  }
};

const n = parseInt(process.argv[2]);
console.log(factorize(n));
