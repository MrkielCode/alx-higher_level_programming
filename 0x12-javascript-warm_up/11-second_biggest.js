#!/usr/bin/node

const args = process.argv.slice(1).map(Number);

let firstMax = -Infinity;
let secondMax = -Infinity;

if (args.length <= 2) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) {
    if (args[i] > firstMax) {
      secondMax = firstMax;
      firstMax = args[i];
    } else if (args[i] < firstMax && args[i] > secondMax) {
      secondMax = args[i];
    }
  }
  console.log(secondMax);
}
