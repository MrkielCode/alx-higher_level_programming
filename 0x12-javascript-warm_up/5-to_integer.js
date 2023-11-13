#!/usr/bin/node
/**
 * to print the number
 */

const args = process.argv[2];

const arg = parseInt(args);

if (!isNaN(arg)) {
  console.log('My number:' + ' ' + arg);
} else {
  console.log('Not a number');
}
