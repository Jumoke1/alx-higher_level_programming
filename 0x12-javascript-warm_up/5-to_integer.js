#!/usr/bin/node
const argv1 = process.argv[2];
const parsedInt = parseInt(argv1);

if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
