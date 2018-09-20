d3.json("/states").then((sampleNames) => {
  console.log(sampleNames)
});

d3.json("/attributes").then((attNames) => {
  console.log(attNames);  
});
var Preferences = [

    {display: "QualityOfLife", value: "QualityofLife" },

    {display: "HealthBehaviours", value: "HealthBehaviours" },

    {display: "ClinicalCare", value: "ClinicalCare" },

    {display: "EconomicFactors", value: "EconomicFactors" },

    {display: "PhysicalEnvironment", value: "PhysicalEnvironment" }

    ];

var states = [
  {display: "Alaska", value: "AK" },
  {display: "Alabama", value: "AL" },
  {display: "Arkansas", value: "AR" },
  {display: "American Samoa", value: "AS" },
  {display: "Arizona", value: "AZ" },
  {display: "California", value: "CA" },
  {display: "Colorado", value: "CO" },
  {display: "Connecticut", value: "CT" },
  {display: "District of Columbia", value: "DC" },
  {display: "Delaware", value: "DE" },
  {display: "Florida", value: "FL" },
  {display: "Georgia", value: "GA" },
  {display: "Guam", value: "GU" },
  {display: "Hawaii", value: "HI" },
  {display: "Iowa", value: "IA" },
  {display: "Idaho", value: "ID" },
  {display: "Illinois", value: "IL" },
  {display: "Indiana", value: "IN" },
  {display: "Kansas", value: "KS" },
  {display: "Kentucky", value: "KY" },
  {display: "Louisiana", value: "LA" },
  {display: "Massachusetts", value: "MA" },
  {display: "Maryland", value: "MD" },
  {display: "Maine", value: "ME" },
  {display: "Michigan", value: "MI" },
  {display: "Minnesota", value: "MN" },
  {display: "Missouri", value: "MO" },
  {display: "Northern Mariana Islands", value: "MP" },
  {display: "Mississippi", value: "MS" },
  {display: "Montana", value: "MT" },
  {display: "North Carolina", value: "NC" },
  {display: "North Dakota", value: "ND" },
  {display: "Nebraska", value: "NE" },
  {display: "New Hampshire", value: "NH" },
  {display: "New Jersey", value: "NJ" },
  {display: "New Mexico", value: "NM" },
  {display: "Nevada", value: "NV" },
  {display: "New York", value: "NY" },
  {display: "Ohio", value: "OH" },
  {display: "Oklahoma", value: "OK" },
  {display: "Oregon", value: "OR" },
  {display: "Pennsylvania", value: "PA" },
  {display: "Puerto Rico", value: "PR" },
  {display: "Rhode Island", value: "RI" },
  {display: "South Carolina", value: "SC" },
  {display: "South Dakota", value: "SD" },
  {display: "Tennessee", value: "TN" },
  {display: "Texas", value: "TX" },
  {display: "Utah", value: "UT" },
  {display: "Virginia", value: "VA" },
  {display: "Virgin Islands", value: "VI" },
  {display: "Vermont", value: "VT" },
  {display: "Washington", value: "WA" },
  {display: "Wisconsin", value: "WI" },
  {display: "West Virginia", value: "WV" },
  {display: "Wyoming", value: "WY" },
];


    
var dropDowns = ["#preference1", "#preference2","#preference3", "#preference4", '#StateShortName'];

  function add_dropdown()  {   
    $(dropDowns).each(function (i) { //populate child options
        if (dropDowns[i] !='#StateShortName') {
          $(dropDowns[i]).html(""); //reset child options    
        Preferences.forEach(function(element) {
            $(dropDowns[i]).append("<option value=\""+element.value+"\">"+element.display+"</option>");
          });
        }
        else {
          console.log("inside #StateShortName");
          $(dropDowns[i]).html(""); //reset child options
          states.forEach(function(element) {
            $(dropDowns[i]).append("<option value=\""+element.value+"\">"+element.display+"</option>");
          });
        }
    });
  };
    


// //If parent option is changed

// $("#parent_selection").change(function() {

//             var parent = $(this).val(); //get option value from parent


//             // switch(parent){ //using switch compare selected option and populate child
//             //            case 'QualityofLife':
//             //                   list(Preferences,'QualityofLife', '#Preference2');
//             //                   break;
//             //            case 'HealthBehaviours':
//             //                   list(Preferences,'HealthBehaviours','#Preference3');
//             //                   break;
//             //            case 'ClinicalCare':
//             //                   list(Preferences,'ClinicalCare','#Preference4');
//             //                   break;
//             //             case 'EconomicFactors':
//             //                   list(Preferences,'EconomicFactors','#Preference5');
//             //                   break;
//             //             case 'PhysicalEnvironment':
//             //                   list(Preferences,'PhysicalEnvironment');
//             //             break;      
//             //          default: //default child option is blank
//             //                   $("#child_selection").html('');
//             //                   break;
//             //    }

// });


// //function to populate child select box

// function list(array_list)

// {

//     $("#child_selection").html(""); //reset child options

//     $(array_list).each(function (i) { //populate child options

//              $("#child_selection").append("<option value=\""+array_list[i].value+"\">"+array_list[i].display+"</option>");

//     });

// }

// function add_dropdown(){ 
    

//     Plotly.d3.json("/names",function(error,response){
//         if(error) console.warn(error);

//         var dropdown_select = Plotly.d3.select("#selDataset");

//        for(var i=0;i<response.length;i++){
//            dropdown_select.append("option").attr("value",response[i]).text(response[i]);
//        }
//        optionChanged(response[0]);
//     })

    
// }

// function optionChanged(selectedValue){
  
//     Plotly.d3.json("/metadata/"+selectedValue,function(error,response){
//         if(error) console.warn(error);

//         var metadata_Sample= Plotly.d3.select(".metadata");

//         // Remove Old metadata 
//         metadata_Sample.selectAll("p").remove();

//         for(var key in response){
//             if(response.hasOwnProperty(key)){
//                 metadata_Sample.append("p").text(key + ":   " + response[key]);
//             }
//         }
//     })

// };

add_dropdown()