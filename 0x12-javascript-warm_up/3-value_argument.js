#!/usr/bin/node

/*
 * prints the arguements passed to it
 */

const args = process.argv;
const arg = args[2];
if (arg) { console.log(arg); } else { console.log('No argument'); }
