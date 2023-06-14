#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
	console.log('Missing number of occurrences');
} else {
	const x = parseInt(process.argv[2]);
	let y = 0;
	while (y < x) {
		console.log('C is fun');
		y++;
	}
}
