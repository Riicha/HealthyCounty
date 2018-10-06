# Web-Health-Index

Standard Score / z-Score. The standard score (more commonly referred to as a z-score) is a very useful statistic because it (a) allows us to 
calculate the probability of a score occurring within our normal distribution and (b) enables us to compare two scores that are 
from different normal distributions.
     
Objective:
How can we quantitively and qualitatively measure the health of a county?
What are the factors that make a county healthy?
How can we select a county based on the health parameters (e.g. air quality or proximity to health centers) that matter to an individual or families?

Approach:
Offer users the flexibility to select state and county of their choice. Based on the selection, display the 5 attributes that we have considered for the project, and respective ranks.
Offer users the flexibility to select state and attribute of their choice, and ability to select one of top 3 counties for the selection
Offer map visualization as a tool to compare and contrast the counties for a selected state

Display & Determinations :-
1. County level health index /score for certain states and provide interactive visualization for users.
2. Suggest top 10 Counties
3. Based on the choice of User's selection of State and Health Attribute preference Top 3 counties is suggested
4. The details of the Top 3 counties include-
    a) Link to Wikipidea
    b) Population
    c) Aggregated values of the z-scores of the Attributes
    d) Latitude
    e) Longitude
5. The calculation is based on:
     a) 40 % weitage to the first attribute + value of the z-Score.
     b) 30 % weitage to the second attribute + value of the z-Score.
     c) 20 % weitage to the third attribute + value of the z-Score.
     d) 10  % weitage to the fourth attribute + value of the z-Score.

Technology Stack:
Presentation Layer: HTML, CSS, Bootstrap
Middleware: Flask
DataBase: MONGODB
Programming Languages: Python, Javascript, Jquery
Vizualization: Leaflet & D3
libraries: glob2, xlrd, Flask, render_template,jsonify, pymongo 
     
     
     

