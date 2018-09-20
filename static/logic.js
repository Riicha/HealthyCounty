
function displayCounties() {
    
    // Get the data from the table displayed from flask 
    var CountyNames = $('.dataframe tr').not(":first").find('td:eq(1)');
    var CountyWikiLinks =   $('.dataframe tr').not(":first").find('td:eq(2)');
    var Latitudes = $('.dataframe tr').not(":first").find('td:eq(3)');
    var Longitudes = $('.dataframe tr').not(":first").find('td:eq(4)');
    var Populations = $('.dataframe tr').not(":first").find('td:eq(5)');
    var TotalAreas = $('.dataframe tr').not(":first").find('td:eq(12)');

    if (CountyNames !=undefined && CountyNames.length > 0 ) {
    
        var container = L.DomUtil.get('map');
        // Need to null the exiting map before reploting it
        if(container != null){
         container._leaflet_id = null;
        }
        
    var myMap = L.map("map", {
        center: [parseFloat(Latitudes[0].innerHTML), parseFloat(Longitudes[0].innerHTML)],
    zoom: 6
    });

    // Add a tile layer
    L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
    }).addTo(myMap);

    // // An array containing each city's name, location, and population
    var cities = [{
    location: [parseFloat(Latitudes[0].innerHTML),parseFloat(Longitudes[0].innerHTML)],
    name: CountyNames[0].innerHTML,
    population: Populations[0].innerHTML
    },
    {
        location: [parseFloat(Latitudes[1].innerHTML),parseFloat(Longitudes[1].innerHTML)],
        name: CountyNames[1].innerHTML,
        population: Populations[1].innerHTML
    },
    {
        location: [parseFloat(Latitudes[2].innerHTML),parseFloat(Longitudes[2].innerHTML)],
        name: CountyNames[2].innerHTML,
        population: Populations[2].innerHTML
    }
    ];


    // Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
    for (var i = 0; i < cities.length; i++) {
    var city = cities[i];
    //  alert("<h1>" + city.name + "</h1> <hr> <h3>Population " + city.population + "</h3>" + city.location[0] + city.location[1]);
    L.marker(city.location)
        .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Population " + city.population + "</h3>")
        .addTo(myMap);
        }
    }
}
displayCounties()

