
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
    
    var html = '<div class="col-md-12">';
    html += '<div class="col-md-1">StateName</div>';
    html += '<div class="col-md-1">CountyName</div>';
    html += '<div class="col-md-1">AggregatedValue</div>';
    html += '<div class="col-md-1">Population</div>';
    html += '<div class="col-md-1">TotalArea</div>';
    html += '<div class="col-md-1">Latitude</div>';
    html += '<div class="col-md-1">Longitude</div>';
    html += '<div class="col-md-4">CountyWikiLink</div>';
    html += '</div>';

    html += '<div class="col-md-12">';
    html += '<div class="col-md-1">' + response[0].StateName + '</div>';
    html += '<div class="col-md-1">' + response[0].CountyName + '</div>';
    html += '<div class="col-md-1">' + response[0].AggregatedValue + '</div>' ;
    html += '<div class="col-md-1">' + response[0].Population + '</div>';
    html += '<div class="col-md-1">' + response[0].TotalArea + '</div>';
    html += '<div class="col-md-1">' + response[0].Latitude + '</div>';
    html += '<div class="col-md-1">' + response[0].Longitude + '</div>';
    html += '<div class="col-md-1">' + response[0].CountyWikiLink + '</div>';
    html += '</div>';

    html += '<div class="col-md-12">';
    html += '<div class="col-md-1">' + response[1].StateName + '</div>';
    html += '<div class="col-md-1">' + response[1].CountyName + '</div>';
    html += '<div class="col-md-1">' + response[1].AggregatedValue + '</div>' ;
    html += '<div class="col-md-1">' + response[1].Population + '</div>';
    html += '<div class="col-md-1">' + response[1].TotalArea + '</div>';
    html += '<div class="col-md-1">' + response[1].Latitude + '</div>';
    html += '<div class="col-md-1">' + response[1].Longitude + '</div>';
    html += '<div class="col-md-1">' + response[1].CountyWikiLink + '</div>';
    html += '</div>';

    html += '<div class="col-md-12">';
    html += '<div class="col-md-1">' + response[2].StateName + '</div>';
    html += '<div class="col-md-1">' + response[2].CountyName + '</div>';
    html += '<div class="col-md-1">' + response[2].AggregatedValue + '</div>' ;
    html += '<div class="col-md-1">' + response[2].Population + '</div>';
    html += '<div class="col-md-1">' + response[2].TotalArea + '</div>';
    html += '<div class="col-md-1">' + response[2].Latitude + '</div>';
    html += '<div class="col-md-1">' + response[2].Longitude + '</div>';
    html += '<div class="col-md-1">' + response[2].CountyWikiLink + '</div>';
    html += '</div>';

    console.log(html);

    $("#uc3Table").append(html);
    var factsUrl = response[0].CountyWikiLink + ' #bodyContent';
    $("#countyFacts").load(factsUrl);
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


function displayTable(top3Counties) {
   
    var html = '<div class="col-md-12">';
    html += '<div class="col-md-1">StateName</div>';
    html += '<div class="col-md-1">CountyName</div>';
    html += '<div class="col-md-1">AggregatedValue</div>';
    html += '<div class="col-md-1">Population</div>';
    html += '<div class="col-md-1">TotalArea</div>';
    html += '<div class="col-md-1">Latitude</div>';
    html += '<div class="col-md-1">Longitude</div>';
    html += '<div class="col-md-4">CountyWikiLink</div>';

    /*['AggregatedValue', 'CountyName', 'CountyWikiLink', 'Latitude',
    'Longitude', 'Population', 'StateLatitude', 'StateLongitude',
    'StateName', 'StateShortName', 'TotalArea']*/

    $.each(top3Counties, function(c,item) {
        console.log(c);
        
        console.log(item[c]);
        console.log(item[c].StateName);
        //alert(c.StateName);
        //alert(item[c][0]);
        //alert(item[0][0]);
        //console.log(item[c].StateName);
        html += '<div class="col-md-1">' + c.StateName + '</div>';
        html += '<div class="col-md-1">' + c.CountyName + '</div>';
        html += '<div class="col-md-1">' + c['AggregatedValue'] + '</div>' ;
        html += '<div class="col-md-1">' + c['Population'] + '</div>';
        html += '<div class="col-md-1">' + c['TotalArea'] + '</div>';
        html += '<div class="col-md-1">' + c['Latitude'] + '</div>';
        html += '<div class="col-md-1">' + c['Longitude'] + '</div>';
        html += '<div class="col-md-1">' + c['CountyWikiLink'] + '</div>';
      });

    
    html += '</div>';

    alert(html);
    $("#uc3Table").append(html);

    
  }

