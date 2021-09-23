$.get('https://fourtonfish.com/hellosalut/?lang=pl', function (data) {
  $('div#hello')
    .append(data.hello);
}, 'json');
