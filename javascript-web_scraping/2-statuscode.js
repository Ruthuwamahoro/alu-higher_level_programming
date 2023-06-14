#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request.get(url,(error,response) => {
    if(error){
        console.log(error)
    }
    console.log(JSON.parse(response.body).title);
});
