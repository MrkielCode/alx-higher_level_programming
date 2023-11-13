#!/usr/bin/node
/**
 * print shape
 */

const intValue = parseInt(process.argv[2]);
let i, j;

if (!isNaN(intValue)) {
  for (i = 0; i < intValue; i++) {
    let x = '';
    for (j = 0; j < intValue; j++) {
      x += 'x';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
