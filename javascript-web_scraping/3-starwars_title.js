#!/usr/bin/node
const variable = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
variable.get(url, (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(response.body).title);
});
