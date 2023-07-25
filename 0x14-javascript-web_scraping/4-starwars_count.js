#!/usr/bin/node
/* prints number of movies where character wedege antilles is */

const req = require('req');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const reslt = JSON.parse(body).reslt;
    console.log(reslt.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
