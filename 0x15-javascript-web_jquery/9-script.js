$.get('https://fourtonfish.com/hellosalut/?lang=ru', function (data) {
  $('div#hello')
    .append(data.hello);
}, 'json');
