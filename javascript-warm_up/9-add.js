#!/usr/bin/node

const first_argv = parseInt(process.argv[2]);
const second_argv = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

if (isNaN(first_argv) || isNaN(second_argv)) {
  console.log('NaN');
} else {
  console.log(add(first_argv, second_argv));
}
