#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const num1 = process.argv.slice(2).map(Number);
  const num2 = num1.sort(
	  function (y, z) {
		  return z - y;
	  })[1];
  console.log(num2);
}
