$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (meow) {
  $('div#character')
  // ye, the data received is called meow. Why? Because I can.
    .append(meow.name);
}, 'json');
