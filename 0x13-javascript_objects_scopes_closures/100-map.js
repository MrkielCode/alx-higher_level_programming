#!/usr/bin/node

const { list } = require('./100-data');
const newList = list.map((num, i) => {
  return num * i;
});
console.log(list);
console.log(newList);
