#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file. */
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (!err) {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(err);
  }
});
