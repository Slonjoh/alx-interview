#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(`Error: ${err.message}`);
    process.exit(1);
  }

  if (res.statusCode !== 200) {
    console.error(`HTTP error! status: ${res.statusCode}`);
    process.exit(1);
  }

  const characterUrls = body.characters;

  characterUrls.forEach(characterUrl => {
    request(characterUrl, { json: true }, (err, res, characterBody) => {
      if (err) {
        console.error(`Error: ${err.message}`);
        return;
      }

      if (res.statusCode !== 200) {
        console.error(`HTTP error! status: ${res.statusCode}`);
        return;
      }

      console.log(characterBody.name);
    });
  });
});
