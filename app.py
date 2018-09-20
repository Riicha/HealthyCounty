import pymongo 
from flask import(Flask, render_template,jsonify, request)
from Data.CountySelection import CountySelection
#------------------------------------------------------------------------------------#
# Flask Setup #
#------------------------------------------------------------------------------------#
app = Flask(__name__)

#------------------------------------------------------------------------------------#
# Local MongoDB connection #
#------------------------------------------------------------------------------------#
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# # create / Use database
db = client.healthi_db

#------------------------------------------------------------------------------------#
# MLab MongoDB connection #
#------------------------------------------------------------------------------------#
# conn = 'mongodb://<add user Pwd here>@ds255332.mlab.com:55332/healthi_db'
# client = pymongo.MongoClient(conn,ConnectTimeoutMS=30000)
# db = client.get_default_database()

#Database connection

# db = client.get_database('healthi_db')

# Home Page
@app.route("/")
def home():
    result = request.form
    for r in request.form:
            print(r)
    return render_template("Landing.html",result = result)

# User selection is sent
@app.route('/attributeSelection',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      selection = {}
      for select in result.items():
            # populate the selection dictionary
            selection[select[0]] = select[1]

      print('user selection')
      print(selection)
    #   Get the Top 3 counties per user selection
      userPref = CountySelection(selection)
      
      userPref = userPref.Selection()
      print(userPref.to_html())
    #   print(userPref.to_html())
    #   Send back the html back to user
      return render_template("Landing.html",result = userPref.to_html())

# Route to display all the five attributes to measure health of a county
@app.route("/attributes")
def attributes():
    sample_list = []
    # db = client.Category
    for item in db.Category.find():
        for cat in item['cat']:
            sample_list.append(cat)
    return jsonify(sample_list)

#Route to display all the states present in the database
@app.route("/states")
def state():
    sample_list = []
    states_list = []
    Statedict={}
    # db = client.State
    for item in db.State.find():
        states_list.append(item['StateName'])
    Statedict['States'] = states_list 
    sample_list.append(Statedict)
    return jsonify(sample_list)  

#Route to display the county names of all the counties present in the given state
@app.route("/countynames/<state>")
def county(state):
    sample_list = []
    # db = client.State
    for item in db.State.find():
        county_list=[]
        County_dict={}
        if item['StateName'].lower() == state.lower():
            State_Counties = item['Counties']
            for County in State_Counties:
                county_list.append(County['County']['CountyName'])
            County_dict['County Names'] = county_list          
            sample_list.append({state.upper() : County_dict})
    return jsonify(sample_list)   

#Route to display all the zscores and rank of all the counties for the given state
@app.route("/zscores/<state>")
def zscore(state):
    sample_list = []
    # db = client.State
    for item in db.State.find():
        if item['StateName'].lower() == state.lower():
            State_Counties = item['Counties']
            for Zscores in State_Counties:              
                sample_list.append({Zscores['County']['CountyName']:{
                    "QualityofLife":Zscores['County']['QualityofLife'],
                    "HealthBehaviours":Zscores['County']['HealthBehaviours'],
                    "ClinicalCare" : Zscores['County']['ClinicalCare'], 
                    "EconomicFactors" : Zscores['County']['EconomicFactors'],
                    "PhysicalEnvironment":Zscores['County']['PhysicalEnvironment']
                }})
    return jsonify(sample_list)            

# Route to display the all the information about the given state    
@app.route("/details/<state>")
def details(state):
    sample_list = []
    # db = client.State
    for item in db.State.find():
        Statedetaildict = {}
        if item['StateName'].lower() == state.lower():
            Statedetaildict['State'] = item['StateName']
            Statedetaildict['Year'] = item['Year']
            Statedetaildict['FIPS'] = item['FIPS']
            Statedetaildict['Counties'] = item['Counties']
            sample_list.append(Statedetaildict)
    return jsonify(sample_list)        

#------------------------------------------------------------------------------------#
# Initiate Flask app
#------------------------------------------------------------------------------------#
if __name__=="__main__":
    #connect_args={'check_same_thread':False}
    app.run(debug=True)

#Pragati : 9/14/2018. Updated to create 4 routes and modified 1 route.
#Tested mlab cloud mongodb as well as with local mongodb. 
# Updated & Tested Riicha : 9/15/2018 Web Scaped & Added # 1. Lat & Long of counties.2. Link to Wiki 
# 3. population & 4. Area etc


#    















################################################################
# from flask import Flask, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def student():
#    return render_template('student.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

# if __name__ == '__main__':
#    app.run(debug = True)