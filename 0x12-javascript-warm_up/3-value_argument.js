#!/usr/bin/node
/**
 * print first arg
 */

const argv = process.argv[2];

if (!argv) {
  console.log('No argument');
} else {
  console.log(argv);
}
