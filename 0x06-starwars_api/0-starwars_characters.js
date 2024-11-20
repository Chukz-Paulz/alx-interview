#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching the movie:', error);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    printCharacters(characters, 0);
  } catch (err) {
    console.error('Error parsing the response:', err);
  }
});


function printCharacters(characters, index) {
  if (index >= characters.length) return;

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error fetching character:', error);
      return;
    }

    try {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      printCharacters(characters, index + 1);
    } catch (err) {
      console.error('Error parsing character data:', err);
    }
  });
}
