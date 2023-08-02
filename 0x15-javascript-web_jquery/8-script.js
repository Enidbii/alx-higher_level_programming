$(function() {
  const url = "https://swapi-api.alx-tools.com/api/films/?format=json";
  $get(url, function(data){
    const titles = data.results;
    for (let j = 0; j < titles.length; j++) {
      $("UL#list_movies").append("<li>" + titles[j].title + "</li>");
    }
  });
});
