console.log("Inside index.js");

var stateselector = d3.select('#StateShortName');

d3.json("/states").then((sampleNames) => {
  console.log("We will win!")  
//   console.log(sampleNames)
  Object.entries(sampleNames).forEach(([key,value])=>{
    console.log("We will definitely win1!")    
    console.log(key,value)
    value.forEach((data)=>{
      stateselector.append("option").text(value).property("value",value)
    });   
  });
});  

//   console.log(typeof(sampleNames))
//   sampleNames.forEach((data)=>{
//       console.log(data)
    //   stateselector.append("option").text(data).property("value",data);
//   }
// )  

var prefselector1 = d3.select('#preference1');
var prefselector2 = d3.select('#preference2');
var prefselector3 = d3.select('#preference3');
var prefselector4 = d3.select('#preference4');
// var prefselector5 = d3.select('#preference5');

d3.json("/attributes").then((attNames) => {
  console.log(attNames)
  console.log(typeof(attNames))
  attNames.forEach((data)=>{
    prefselector1.append("option").text(data).property("value",data)
    prefselector2.append("option").text(data).property("value",data)
    prefselector3.append("option").text(data).property("value",data)
    prefselector4.append("option").text(data).property("value",data)
    //prefselector5.append("option").text(data).property("value",data)
  })
  
});


