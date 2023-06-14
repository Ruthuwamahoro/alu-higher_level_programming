#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body);
  const moviesWithWedge = films.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );
  console.log(moviesWithWedge);
});
