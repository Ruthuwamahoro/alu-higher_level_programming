#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];
fs.writeFile(filePath, stringToWrite,'utf8',function(err){
    if (err){
        console.error(error);
    }
});
