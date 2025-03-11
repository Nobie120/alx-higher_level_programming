#!/usr/bin/node

class Rectangle {

	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		if (this.height && this.width) {
			for (let i = 0; i < thi.height; i++) {
				console.log('X'.repeat(this.width));
			}
		}
	}

	rotate () {
		let temp = this.height;
		this.height = this.width;
		this.width = this.tempt;
	}

	double () {
		this.height *= 2;
		this.width *= 2;
	}
}

module.exports = Rectangle;
