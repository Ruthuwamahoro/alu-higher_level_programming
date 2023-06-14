#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
if (!filePath) {
  console.error("no such file or directory");
}
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.err(err);
  }
  console.log(data);
});
