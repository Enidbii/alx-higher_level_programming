#!/usr/bin/node
/* prints star wars movie where ep no. matches int */

const req = require('req');
const epNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

req(API_URL + epNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
