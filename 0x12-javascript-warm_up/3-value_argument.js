#!/usr/bin/node
/**
 * print first arg
 */

const argv = process.argv[2];

if (!argv) {
  console.log('No arguments');
} else {
  console.log(argv);
}
