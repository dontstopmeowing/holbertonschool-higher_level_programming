#!/usr/bin/node
const lengthz = process.argv.length;
if (lengthz < 3) {
  console.log('No argument');
} else if (lengthz === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
