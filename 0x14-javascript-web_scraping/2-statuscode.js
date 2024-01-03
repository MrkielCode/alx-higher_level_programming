#!/usr/bin/node
/**
 * script to send request and print out the status code
 */

const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode === 200) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(`doesnt_exist\ncode: ${response.statusCode}`);
  }
});
