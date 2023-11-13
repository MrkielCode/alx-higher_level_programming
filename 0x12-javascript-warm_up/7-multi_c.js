#!/usr/bin/node
/**
 * print C is fun based
 * on argv passed
 */

let i;
const intValue = parseInt(process.argv[2]);

if (!isNaN(intValue)) {
  for (i = 0; i < intValue; i++) {
    console.log('C is fun');
  }
} else {
  console.log('“Missing number of occurrences”');
}
