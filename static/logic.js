
function displayCounties() {
    console.log('CountyNames');
  
    var userSelection = '';

    userSelection ='StateShortName_';
    userSelection +=$('#StateShortName option:selected').val();
    userSelection +=':preference1_';
    userSelection +=$('#Preference1 option:selected').val();
    userSelection +=':preference2_';
    userSelection +=$('#Preference2 option:selected').val();
    userSelection +=':preference3_';
    userSelection +=$('#Preference3 option:selected').val();
    userSelection +=':preference4_';
    userSelection +=$('#Preference4 option:selected').val();
    
    console.log(userSelection);

    var userSelectionUrl = `/attributeSelection/${userSelection}`;

    Plotly.d3.json(userSelectionUrl, function(error, response){

       console.log(response); 
        if (error) {
          return console.log(error);
        }
 
    if (response !=undefined && response.length > 0 ) {
    console.log(response);
    
    var html = '<table style="width:100%" id="uc3" class="table table-hover" >';
    html += '<tr>';
    
    html += '<td style="color: orange">StateName</td>';
    html += '<td style="color: orange">CountyName</td>';
    html += '<td style="color: orange">AggregatedValue</td>';
    html += '<td style="color: orange">Population</td>';
    html += '<td style="color: orange">TotalArea</td>';
    html += '<td style="color: orange">Latitude</td>';
    html += '<td style="color: orange">Longitude</td>';
    html += '<td style="color: orange">CountyWikiLink</td>';
    html += '</tr>';
    
    html += '<tr>';    
    html += '<td>' + response[0].StateName + '</td>';
    html += '<td>' + response[0].CountyName + '</td>';
    html += '<td>' + response[0].AggregatedValue.toFixed(5) + '</td>' ;
    html += '<td>' + response[0].Population + '</td>';
    html += '<td>' + response[0].TotalArea + '</td>';
    html += '<td>' + response[0].Latitude + '</td>';
    html += '<td>' + response[0].Longitude + '</td>';
    html += '<td> <div class="countyData"> <a { color: inherit; }  href="' + response[0].CountyWikiLink + '"  target="_blank">' + response[0].CountyName +'</div>' +' </td>';
    html += '</tr>';

    html += '<tr>';    
    html += '<td>' + response[1].StateName + '</td>';
    html += '<td>' + response[1].CountyName + '</td>';
    html += '<td>' + response[1].AggregatedValue.toFixed(5) + '</td>' ;
    html += '<td>' + response[1].Population + '</td>';
    html += '<td>' + response[1].TotalArea + '</td>';
    html += '<td>' + response[1].Latitude + '</td>';
    html += '<td>' + response[1].Longitude + '</td>';
    html += '<td class="linkFill"> <div class="countyData"> <a { color: inherit; }  href="' + response[1].CountyWikiLink + '"  target="_blank">' + response[1].CountyName +'</div>' +' </td>';
    html += '</tr>';

    html += '<tr>';    
    html += '<td>' + response[2].StateName + '</td>';
    html += '<td>' + response[2].CountyName + '</td>';
    html += '<td>' + response[2].AggregatedValue.toFixed(5) + '</td>' ;
    html += '<td>' + response[2].Population + '</td>';
    html += '<td>' + response[2].TotalArea + '</td>';
    html += '<td>' + response[2].Latitude + '</td>';
    html += '<td>' + response[2].Longitude + '</td>';
    html += '<td> <div class="countyData"> <a { color: inherit; } href="' + response[2].CountyWikiLink + '"  target="_blank">' + response[2].CountyName +'</div>' +' </td>';
    html += '</tr>';

    html += '</table>';

    $("#uc3Table").html("");
    $("#uc3Table").append(html);
    /*['AggregatedValue', 'CountyName', 'CountyWikiLink', 'Latitude',
    'Longitude', 'Population', 'StateLatitude', 'StateLongitude',
    'StateName', 'StateShortName', 'TotalArea']*/

    
    
    
    // displayTable(response);

    //var county_specs = response[0].Counties;

    // Get the data from the table displayed from flask 
    /*var CountyNames = response[0]['CountyName'];
    var CountyWikiLinks =   response[0]['CountyWikiLink'];
    var Latitudes = response[0]['Latitude'];
    var Longitudes = response[0]['Longitude'];
    var Populations = response[0]['Population']
    var TotalAreas = response[0]['TotalArea'];
 */
    
        var container = L.DomUtil.get('map');
        // Need to null the exiting map before reploting it
        if(container != null){
         container._leaflet_id = null;
        }
        
    var myMap = L.map("map", {
        center: [parseFloat(response[0].Latitude), parseFloat(response[0].Longitude)],
    zoom: 6
    });

    console.log(myMap);

    // Add a tile layer
    L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 6,
    id: "mapbox.streets",
    accessToken:"pk.eyJ1Ijoic3NhdHBhdGh5IiwiYSI6ImNqbGVjb2I2NzBrbmIzcXBtMDdsOHp5aDcifQ.HCxHkdXAzE7YAK_FCbdUXQ"
    // accessToken: "pk.eyJ1Ijoia3VsaW5pIiwiYSI6ImNpeWN6bjJ0NjAwcGYzMnJzOWdoNXNqbnEifQ.jEzGgLAwQnZCv9rA6UTfxQ"
    }).addTo(myMap);

    // // An array containing each city's name, location, and population
    var cities = [{
    location: [parseFloat(response[0].Latitude),parseFloat(response[0].Longitude)],
    name: response[0].CountyName,
    population: response[0].Population
    },
    {
        location: [parseFloat(response[1].Latitude),parseFloat(response[1].Longitude)],
        name: response[1].CountyName,
        population: response[1].Population
    },
    {
        location: [parseFloat(response[2].Latitude),parseFloat(response[2].Longitude)],
        name: response[2].CountyName,
        population: response[2].Population
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
    })
}




