#!/usr/bin/node
/* Script that display status code of a GET request */

const req = require('req');
req.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
