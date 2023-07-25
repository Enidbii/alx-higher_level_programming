#!/usr/bin/node
/* reads and prints the content of a file */

const file = require('file');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data.toString());
});
