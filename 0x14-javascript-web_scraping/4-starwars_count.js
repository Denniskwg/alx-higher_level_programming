#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < res.results.length; i++) {
      for (let j = 0; j < res.results[i].characters.length; j++) {
        const arr = res.results[i].characters[j].split('/');
        if (arr[arr.length - 2] === '18') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
