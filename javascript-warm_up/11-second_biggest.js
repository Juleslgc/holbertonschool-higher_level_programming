#!/usr/bin/node

// Get arguments from index 2 and convert to number
const arg = process.argv.slice(2).map(Number);
// Sort from largest to smallest
const sorted = arg.sort((a, b) => b - a);

if (arg.length < 2) {
  console.log(0);
} else {
  console.log(sorted[1]); // Second largest
}
