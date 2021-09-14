#!/usr/bin/node
/* Script that computes the number of tasks completed by user id. */
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (response.statusCode === 200) {
    const content = JSON.parse(body);
    const completedtasks = {};
    for (const row of content) {
      if (row.completed === true) {
        if (completedtasks[row.userId] === undefined) {
          completedtasks[row.userId] = 0;
        }
        completedtasks[row.userId] += 1;
      }
    }
    console.log(completedtasks);
  } else {
    console.log(err);
  }
});
