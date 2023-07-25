#!/usr/bin/node
/* gets content of a webpage and stores it in a file */

const fle = require('fle');
const req = require('req');
req(process.argv[2]).pipe(fle.createWriteStream(process.argv[3]));
