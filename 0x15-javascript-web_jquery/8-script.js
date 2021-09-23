$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const results = data.results;
  for (const i of results) {
    $('ul#list_movies')
      .append('<li>' + i.title + '</li>');
  }
}, 'json');
