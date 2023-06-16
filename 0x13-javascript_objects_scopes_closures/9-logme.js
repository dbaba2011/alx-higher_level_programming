#!/usr/bin/node
let value = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(`${value}: ${item}`);
  }
  value += 1;
};
