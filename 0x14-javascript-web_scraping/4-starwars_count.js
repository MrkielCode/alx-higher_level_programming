#!/usr/bin/node
/**
 * get specitfy move characters
 *
 */
const request = require('request');

const apiUrl = process.argv[2];

function getFilms (apiUrl) {
  request(apiUrl, function (error, response, body) {
    if (error) {
      console.log(error);
      return;
    }

    if (response.statusCode === 200) {
      const datas = JSON.parse(body).results;
      const characterWedges = datas.filter(movie =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );
      console.log(characterWedges.length);
    }
  });
}

getFilms(apiUrl);
