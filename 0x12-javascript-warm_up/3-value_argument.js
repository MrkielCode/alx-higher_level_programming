#!/usr/bin/node
/**
 * print first arg
 */

const argv = process.argv;

if (!argv[2]) {
  console.log('No arguments');
} else {
  console.log(argv[2]);
}
