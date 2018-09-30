#-----------------Import Dependencies----------------------------# 
import xlrd
from glob2 import glob
import json
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
import string
import re
# from ScrapedCounty import County





#--------------------------------------------------------------------------------#
def CreateMongoDataBase():
        scrapedCounties = {}  
        ## https://inkplant.com/code/state-latitudes-longitudes
        statesOfUSA = {
        'AK': { "StateName": 'Alaska' , "Latitude" : 61.370716 , "Longitude": -152.404419  },
        'AL': { "StateName": 'Alabama' , "Latitude" : 32.806671 , "Longitude": -86.791130  } ,
        'AR': { "StateName": 'Arkansas' , "Latitude" : 34.969704 , "Longitude": -92.373123  },
        'AZ': { "StateName": 'Arizona' , "Latitude" : 33.729759 , "Longitude": -111.431221 } ,
        'CA': { "StateName": 'California' , "Latitude" : 36.116203 , "Longitude": -119.681564 } ,
        'CO': { "StateName": 'Colorado' , "Latitude" : 39.059811 , "Longitude": -105.311104 },
        'CT': { "StateName": 'Connecticut' , "Latitude" : 41.597782 , "Longitude": -72.755371 } ,
        'DC': { "StateName": 'District of Columbia' , "Latitude" : 38.897438 , "Longitude": -77.026817 },
        'DE': { "StateName": 'Delaware' , "Latitude" : 39.318523 , "Longitude": -75.507141 },
        'FL': { "StateName": 'Florida' , "Latitude" : 27.766279 , "Longitude": -81.686783 },
        'GA': { "StateName": 'Georgia' , "Latitude" : 33.040619 , "Longitude": -83.643074 },
        'HI': { "StateName": 'Hawaii' , "Latitude" : 21.094318 , "Longitude": -157.498337 },
        'IA': { "StateName": 'Iowa' , "Latitude" : 42.011539 , "Longitude": -93.210526 },
        'ID': { "StateName": 'Idaho' , "Latitude" : 	44.240459 , "Longitude": -114.478828 },
        'IL': { "StateName": 'Illinois' , "Latitude" : 40.349457 , "Longitude":-88.986137 },
        'IN': { "StateName": 'Indiana' , "Latitude" : 39.849426 , "Longitude": -86.258278 },
        'KS': { "StateName": 'Kansas' , "Latitude" : 38.526600, "Longitude": -96.726486 },
        'KY': { "StateName": 'Kentucky' , "Latitude" : 37.668140 , "Longitude": -84.670067 },
        'LA': { "StateName": 'Louisiana' , "Latitude" : 31.169546, "Longitude": -91.867805},
        'MA': { "StateName": 'Massachusetts' , "Latitude" : 42.230171, "Longitude": -71.530106},
        'MD': { "StateName": 'Maryland' , "Latitude" : 39.063946, "Longitude": -76.802101},
        'ME': { "StateName": 'Maine' , "Latitude" : 44.693947, "Longitude": -69.381927},
        'MI': { "StateName": 'Michigan' , "Latitude" : 43.326618, "Longitude": -84.536095},
        'MN': { "StateName": 'Minnesota' , "Latitude" : 45.694454 , "Longitude": -93.900192},
        'MO': { "StateName": 'Missouri' , "Latitude" : 38.456085, "Longitude": -92.288368},
        'MS': { "StateName": 'Mississippi' , "Latitude" : 32.741646 , "Longitude": -89.678696 },
        'MT': { "StateName": 'Montana' , "Latitude" : 46.921925, "Longitude": -110.454353},
        'NC': { "StateName": 'North Carolina' , "Latitude" : 35.630066, "Longitude": -79.806419},
        'ND': { "StateName": 'North Dakota' , "Latitude" : 47.528912, "Longitude": -99.784012},
        'NE': { "StateName": 'Nebraska' , "Latitude" : 41.125370, "Longitude": -98.268082},
        'NH': { "StateName": 'New Hampshire' , "Latitude" : 43.452492, "Longitude": -71.563896},
        'NJ': { "StateName": 'New Jersey' , "Latitude" : 40.298904 , "Longitude": -74.521011 } ,
        'NM': { "StateName": 'New Mexico', "Latitude" : 34.840515, "Longitude": -106.248482},
        'NV': { "StateName": 'Nevada' , "Latitude" : 38.313515, "Longitude": -117.055374},
        'NY': { "StateName": 'New York' , "Latitude" : 42.165726 , "Longitude": -74.948051 } ,
        'OH': { "StateName": 'Ohio' , "Latitude" : 40.388783, "Longitude": -82.764915},
        'OK': { "StateName": 'Oklahoma', "Latitude" : 35.565342, "Longitude": -96.928917},
        'OR': { "StateName": 'Oregon' , "Latitude" : 44.572021, "Longitude": -122.070938},
        'PA': { "StateName": 'Pennsylvania' , "Latitude" : 40.590752, "Longitude": -77.209755},
        'RI': { "StateName": 'Rhode Island' , "Latitude" : 41.680893, "Longitude": -71.511780},
        'SC': { "StateName": 'South Carolina' , "Latitude" : 33.856892, "Longitude": -80.945007},
        'SD': { "StateName": 'South Dakota' , "Latitude" : 44.299782 , "Longitude": -99.438828},
        'TN': { "StateName": 'Tennessee' , "Latitude" : 33.040619 , "Longitude": -86.692345},
        'TX': { "StateName": 'Texas' , "Latitude" : 31.054487, "Longitude": -97.563461},
        'UT': { "StateName": 'Utah' , "Latitude" : 40.150032, "Longitude": -111.862434},
        'VA': { "StateName": 'Virginia', "Latitude" : 37.769337, "Longitude": -78.169968},
        'VT': { "StateName": 'Vermont' , "Latitude" : 44.045876, "Longitude": -72.710686},
        'WA': { "StateName": 'Washington', "Latitude" : 47.400902, "Longitude": -121.490494},
        'WI': { "StateName": 'Wisconsin' , "Latitude" : 44.268543, "Longitude": -89.616508},
        'WV': { "StateName": 'West Virginia' , "Latitude" : 38.491226, "Longitude": -80.954453},
        'WY': { "StateName": 'Wyoming' , "Latitude" : 42.755966, "Longitude": -107.302490}
        }


        filePath = ""
        
        # Scrap the counties and store in the dictionary for lookup
        website_url = requests.get("https://en.wikipedia.org/w/index.php?title=User:Michael_J/County_table&oldid=368803236").text
        wikiBaseURL = "https://en.wikipedia.org"

        Soup = BeautifulSoup(website_url,'lxml')
        CountyGeoLocTbl = Soup.find('table',{'class':'wikitable sortable'})
        # Perform lookup from the scraped data for the geo 
        # locations and other facts
        # skip the first row of the scraped data as it is the header.
        for tr in CountyGeoLocTbl.find_all('tr')[1:]:
            tds = tr.find_all('td')
            # Removed the superscripts e.g '[4]' with '' by usage of Regex
            ScrapedCounty = re.compile('[a-zA-Z ]{6,}',re.I).findall(tds[3].text.strip())

            CountyWikiLink = wikiBaseURL + tds[3].a.get('href')
            # Check for blanks / '' in  scraped county
            if (len(ScrapedCounty)>0):
                ScrapedCounty = ScrapedCounty[0].rstrip().lstrip()
            else:
                ScrapedCounty = tds[3].text.strip()

            # if ( tds[1].text in statesOfUSA and isinstance(statesOfUSA[tds[1].text],dict)):
            data = {"StateShortName": tds[1].text,
                        "CountyName" : ScrapedCounty, 
                        "Population" : tds[5].text,
                        "TotalArea" : tds[11].text,
                        "Latitude" : tds[12].text.strip(),
                        "Longitude" : tds[13].text.strip(),
                        "CountyWikiLink":  CountyWikiLink,
                        "StateLatitude" : statesOfUSA[tds[1].text]["Latitude"],
                        "StateLongitude" : statesOfUSA[tds[1].text]["Longitude"],
                }
            #     # Add to dictiory for quick retrival
            scrapedCounties[data["StateShortName"]+data["CountyName"]] = data
            # if (tds[1].text =='NJ'):
            #     print(ScrapedCounty)
       
        xlsFilesOnly = glob(filePath+"*.xls") # parse all xls file(s) only
        StateList = []
        for xlsfile in xlsFilesOnly:
            yearReported = xlsfile[:4]
            wb = xlrd.open_workbook(xlsfile,ragged_rows = True) 
            if (wb != None):    
                sh = wb.sheet_by_name('OutcomesFactorsSubRankings') 
                CountyList = []
                if (sh != None): 
                    for row_index in range(sh.nrows):
                        HealthyCounty = {}
                        if(row_index > 2 ):
                            
                            StateShortName = sh.cell(row_index, 13 ).value
                            CountyName = sh.cell(row_index, 2 ).value
                            
                            StateName = sh.cell(row_index, 1 ).value 

                            QualityofLife = { 
                                "Z-Score" : sh.cell(row_index, 3 ).value,
                                "Rank" : sh.cell(row_index, 4 ).value,
                            }   

                            HealthBehaviours = {
                                "Z-Score" : sh.cell(row_index, 5 ).value,
                                "Rank" : sh.cell(row_index, 6 ).value,
                            }                         

                            ClinicalCare = {
                                "Z-Score" : sh.cell(row_index, 7 ).value,
                                "Rank" : sh.cell(row_index, 8 ).value,
                            }

                            EconomicFactors = {
                                "Z-Score" : sh.cell(row_index, 9 ).value,
                                "Rank" : sh.cell(row_index, 10 ).value,
                            }


                            PhysicalEnvironment = { 
                                "Z-Score" : sh.cell(row_index, 11 ).value,
                                "Rank" : sh.cell(row_index, 12 ).value,
                            }
                            
                            # Make sure we have the county exists in dictionary
                            if (StateShortName + CountyName in scrapedCounties): 
                                c = scrapedCounties[StateShortName + CountyName]
                                # Perform lookup from the scraped data for the geo 
                                # Populate the county dictionary
                                HealthyCounty = {
                                            "CountyName" : CountyName,
                                            "County FIPS" : sh.cell(row_index, 0 ).value,
                                            "QualityofLife": QualityofLife,
                                            "HealthBehaviours" : HealthBehaviours,
                                            "ClinicalCare" : ClinicalCare,
                                            "EconomicFactors" : EconomicFactors,
                                            "PhysicalEnvironment" : PhysicalEnvironment,
                                            "Population" : c["Population"],
                                            "TotalArea" : c["TotalArea"],
                                            "Latitude" : c["Latitude"],
                                            "Longitude" : c["Longitude"],
                                            "CountyWikiLink" :c["CountyWikiLink"],
                                            "StateLatitude": c["StateLatitude"],
                                            "StateLongitude": c["StateLongitude"]
                                        }
                                County = {
                                            "County" : HealthyCounty
                                        }
                                        # Add only when we have found the facts on the county
                                CountyList.append(County)
                                

                    if(row_index == sh.nrows - 1):
                        State = {
                                    "StateName":StateName,
                                    "StateShortName" : StateShortName,
                                    "Year" : yearReported,
                                    "FIPS":sh.cell(row_index, 0 ).value,
                                    "Counties" : CountyList                      
                                }
                        StateList.append(State)
        
        #Creating a json file to display the jsonified data                
        jsonfile = "StateCountyData" + '.json'
        with open(jsonfile, 'w') as f:
            json.dump(StateList, f, indent = 4)

        jsonfile = "ScrappedStateCountyData" + '.json'
        with open(jsonfile, 'w') as f:
            json.dump(scrapedCounties, f, indent = 4)


        #Connection for local host
        conn = 'mongodb://localhost:27017'
        client = pymongo.MongoClient(conn)
        db=client.healthi_db
        
        ## Connection for remote host
        # conn = 'mongodb://<dbuser>:<dbpassword>@ds255332.mlab.com:55332/healthi_db'
        # conn = 'mongodb://Riicha:mlabpolkA#1122@ds113873.mlab.com:13873/healthi_db'
        # client = pymongo.MongoClient(conn,ConnectTimeoutMS=30000)
        # db = client.get_default_database()

        #create list of categories
        Category = ["QualityofLife","EconomicFactors","ClinicalCare","HealthBehaviours","PhysicalEnvironment"]
        #Create a dictionary with the list Category.
        dropdown = {"cat" : Category }

        #drop/create collection Category
        db.Category.drop()
        category = db.Category
        #insert into Category collection
        category.insert(dropdown)

        #drop/create collection State.
        db.State.drop()
        state = db.State
        #insert into State collection
        state.insert_many(StateList)
        # result = state.insert_many(StateList)
        # print("Multiple States {0}".format(result.inserted_ids))
        
CreateMongoDataBase()


        



