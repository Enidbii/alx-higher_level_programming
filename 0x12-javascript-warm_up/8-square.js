#!/usr/bin/node
if (isNaN(process.argv[2] || process.argv[2] === undefined)) {
  console.log('Missing size');
} else {
  const z = parseInt(process.argv[2]);
  let y = 0;
  while (y < z) {
    console.log('X'.repeat(z));
    y++;
  }
}
