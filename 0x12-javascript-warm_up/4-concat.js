#!/usr/bin/node

/*
 *  prints two arguments passed to it, in the following format: “ is ”
 */

const args = process.argv;
const arg = args[2] + ' is ' + args[3];
console.log(arg);
