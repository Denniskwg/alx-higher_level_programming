#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const res = JSON.parse(body);
    const obj = {};
    let count = 0;
    let id = 1;
    for (let i = 0; i < res.length; i++) {
      if (res[i].userId === id) {
        if (res[i].completed === true) {
          count++;
        }
      } else {
        obj[id] = count;
        if (res[i].completed === true) {
          count = 1;
        } else {
          count = 0;
        }
        id++;
      }
    }
    obj[id] = count;
    console.log(obj);
  }
});
