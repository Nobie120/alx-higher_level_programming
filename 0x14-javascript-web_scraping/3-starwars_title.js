#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request.get(url + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode == 200) {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  } else {
    console.log('Error code' + response.statusCode);
  }
});
