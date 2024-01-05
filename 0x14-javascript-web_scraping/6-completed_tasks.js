#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const completedTask = {};
    data.forEach(task => {
      if (task.completed) {
        if (completedTask[task.userId]) {
          completedTask[task.userId]++;
        } else {
          completedTask[task.userId] = 1;
        }
      }
    });

    console.log(completedTask);
  }
});
