#!/usr/bin/node

const size = parseInt(process.argv[2]);
let str;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    str = '';
    for (let j = 0; j < size; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
