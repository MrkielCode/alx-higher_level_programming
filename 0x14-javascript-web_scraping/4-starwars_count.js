#!/usr/bin/node
/**
 * get specitfy move characters
 *
 */
const request = require('request');
const fs = require('fs')
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
        movie.characters.some(character =>
          character.endsWith('/18/')
        )
      );
      console.log(characterWedges.length);
    }
  });
}

getFilms(apiUrl);
