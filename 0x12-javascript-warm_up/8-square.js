#!/usr/bin/node
/**
 * print shape
 */

const intValue = parseInt(process.argv[2]);
let i, j;

if (!isNaN(intValue)) {
  for (i = 0; i < intValue; i++) {
    for (j = 0; j < intValue; j++) {
      process.stdout.write('#');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
