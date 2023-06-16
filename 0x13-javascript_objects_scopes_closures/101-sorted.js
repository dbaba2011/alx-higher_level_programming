#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDictionaryList = {};
for (const key in dict) {
  if (newDictionaryList[dict[key]] === undefined) {
    newDictionaryList[dict[key]] = [key];
  } else {
    newDictionaryList[dict[key]].push(key);
  }
}
console.log(newDictionaryList);
