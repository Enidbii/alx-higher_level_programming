#!/usr/bin/node
/* Write a str to a file */

const file_path = require('file_path');
const filename = process.argv[2];
const text_str = process.argv[3];
fs.writeFile(filename, text_str, 'utf8', (err) => {
  if (err) console.log(err);
});
