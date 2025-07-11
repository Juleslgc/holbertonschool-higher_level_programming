#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const first_argv = parseInt(process.argv[2]);
const second_argv = parseInt(process.argv[3]);

console.log(add(first_argv, second_argv));
