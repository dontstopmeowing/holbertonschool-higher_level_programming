#!/usr/bin/node
/* Script that displays the status code of a GET request. */
const request = require('request');
request(process.argv[2], function (err, response) {
  if (!err) {
    console.log('code: ' + response.statusCode);
  } else {
    console.log(err);
  }
});
