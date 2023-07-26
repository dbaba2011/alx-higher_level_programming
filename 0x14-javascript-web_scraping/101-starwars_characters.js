#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    const characterNames = [];

    let completedRequests = 0;

    characterUrls.forEach((characterUrl, index) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const characterData = JSON.parse(charBody);
          characterNames[index] = characterData.name;
        }

        completedRequests++;

        if (completedRequests === characterUrls.length) {
          characterNames.forEach((characterName) => {
            console.log(characterName);
          });
        }
      });
    });
  }
});
