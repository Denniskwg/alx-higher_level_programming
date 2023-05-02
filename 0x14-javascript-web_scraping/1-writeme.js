#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const str = process.argv[3];
fs.appendFile(file, str, function (err) {
  if (err) {
    console.log(err);
  }
});
