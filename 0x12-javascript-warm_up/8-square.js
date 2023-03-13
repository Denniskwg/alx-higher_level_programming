#!/usr/bin/node
const num = Number(process.argv[2]);
const arr = [];
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < num; j++) {
    arr.push('X');
  }
  for (let i = 0; i < num; i++) {
    console.log(arr.join(''));
  }
}
