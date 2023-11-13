#!/usr/bin/node
/**
 * print first arg
 */

let argv = process.argv[2];

if (!argv) {
  console.log('No arguments');
} else {
  console.log(argv);
}
