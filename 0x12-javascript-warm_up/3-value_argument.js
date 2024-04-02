#!/usr/bin/node
const numArgs = process.argv[2];
const message = numArgs !== undefined ? numArgs : 'No argument';
console.log(message);
