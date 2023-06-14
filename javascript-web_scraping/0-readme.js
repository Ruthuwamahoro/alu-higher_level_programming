#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', (err, content) => {
  if (err) {
    if (err.code === 'ENOENT') {
      console.error(`${filePath} doesn't exist`);
    } else {
      console.error(err);
    }
  }

  console.log(`File content:\n${data}`);
});
