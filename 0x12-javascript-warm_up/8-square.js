#!/usr/bin/node
/**
 * print shape
 */

const intValue = parseInt(process.argv[2]);

if (!isNaN(intValue)) {
  for (let i = 0; i < intValue; i++) {
    let x = '';
    for (let j = 0; j < intValue; j++) {
      x += 'X';
    }
    console.log(x);
  }
} else {
  console.log('Missing size');
}
