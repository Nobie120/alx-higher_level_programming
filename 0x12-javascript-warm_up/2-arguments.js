#!/usr/bin/node

const args = process.argv.slice(2);

if (args < 2) {
	console.log("No arguement")
}else {
	console.log(args[0])
}
