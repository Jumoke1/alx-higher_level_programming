#!/usr/bin/node
const numArgs = process.argv.length;
console.log(numArgs === 0 ? 'No argument' : numArgs === 1 ? 'Argument found' : 'Arguments found');
