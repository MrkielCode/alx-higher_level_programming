#!/usr/bin/node
/**
 * sum numbers
 */

function add (a, b) {
  const first = parseInt(a);
  const second = parseInt(b);
  if (isNaN(first) || isNaN(second)) {
    console.log('NaN');
  } else {
    console.log(first + second);
  }
}
add(process.argv[2], process.argv[3]);
