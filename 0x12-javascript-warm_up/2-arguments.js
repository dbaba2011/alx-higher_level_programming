#!/usr/bin/node

const test = process.argv.length;
if (test <= 2) {
  console.log('No argument');
} else if (test === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
