from pymongo import MongoClient
import pandas as pd
import requests
from bs4 import BeautifulSoup

class CountySelection:
    def __init__(self, preferences):
        self.StateShortName = preferences['StateShortName']
        self.Preference1 = preferences['preference1']
        self.Preference2 = preferences['preference2']
        self.Preference3 = preferences['preference3']
        self.Preference4 = preferences['preference4']

    
    
    def Selection(self):
        #Connection for local host
        conn = 'mongodb://localhost:27017'
        client = MongoClient(conn)
        db=client.healthi_db
        ## Connection for remote host
        # conn = 'mongodb://<dbuser>:<dbpassword>@ds255332.mlab.com:55332/healthi_db'
        # conn = 'mongodb://Riicha:mlabpolkA#1122@ds113873.mlab.com:13873/healthi_db'
        # client = pymongo.MongoClient(conn,ConnectTimeoutMS=30000)
        # db = client.get_default_database()
        
        # TBD Need to use aggregate function to optimize
        # aggregate([
        #              { $match: { status: "A" } },
        #              { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
        #              { $sort: { total: -1 } }
        #            ])
        Counties = []
        top1County = 1
        for item in db.State.find({'StateShortName': self.StateShortName}): 
            for c in item['Counties']:
                if ( 'StateLatitude' in c['County']):
                    StateLatitude= float(c['County']['StateLatitude'])
                if ( 'StateLongitude' in c['County']):
                    StateLongitude= float(c['County']['StateLongitude'])       

                AggregatedValue  = 0.0    
                if (type( c['County'] [self.Preference1]['Z-Score']) == float  ):
                   AggregatedValue +=(c['County'] [self.Preference1]['Z-Score']) * 0.4
                else:
                   if (c['County'] [self.Preference1]['Z-Score'].strip() !=''):
                    AggregatedValue +=float(c['County'] [self.Preference1]['Z-Score'].strip()) * 0.4 
                
                if (type( c['County'] [self.Preference2]['Z-Score']) == float  ):
                   AggregatedValue +=(c['County'] [self.Preference2]['Z-Score']) * 0.3
                else:
                   if (c['County'] [self.Preference2]['Z-Score'].strip() !=''):
                    AggregatedValue +=float(c['County'] [self.Preference2]['Z-Score'].strip()) * 0.3 
                
                if (type( c['County'] [self.Preference3]['Z-Score']) == float  ):
                   AggregatedValue +=(c['County'] [self.Preference3]['Z-Score']) * 0.2
                else:
                   if (c['County'] [self.Preference3]['Z-Score'].strip() !=''):
                    AggregatedValue +=float(c['County'] [self.Preference3]['Z-Score'].strip()) * 0.2 
                
                if (type( c['County'] [self.Preference4]['Z-Score']) == float  ):
                   AggregatedValue +=(c['County'] [self.Preference4]['Z-Score']) * 0.1
                else:
                   if (c['County'] [self.Preference4]['Z-Score'].strip() !=''):
                    AggregatedValue +=float(c['County'] [self.Preference4]['Z-Score'].strip()) * 0.1 
                

                county = {  'StateName': item['StateName'],
                            'StateShortName' : self.StateShortName,
                            'CountyName'  : c['County']['CountyName'],
                            'TotalArea' : c['County']['TotalArea'],
                            'Population': c['County']['Population'],
                            'Latitude': float(c['County']['Latitude'][:-1].strip()[1:]),
                            'Longitude': float(c['County']['Longitude'][:-1].strip().replace('–', '-')),
                            'CountyWikiLink': c['County']['CountyWikiLink'],
                            'AggregatedValue' : AggregatedValue,
                            "StateLatitude":StateLatitude,
                            "StateLongitude":StateLongitude                    
                        }
                if (top1County == 1):
                  website_url = requests.get(c['County']['CountyWikiLink']).text
                 
                  Soup = BeautifulSoup(website_url,'lxml')
                  CountyGeoLocTbl = Soup.find('div', {'id':'bodyContent'})
                  county['CountyFacts'] = CountyGeoLocTbl      
                # Add the county to the collection
                Counties.append(county)
                top1County +=1 
        # Populate the dataframe
        df = pd.DataFrame(Counties).reset_index(drop=True)
        if ( len(Counties)> 0) :
            df= df.sort_values(by=['AggregatedValue'], ascending=[True] )
        top3 = df.head(3)

        return top3


# p1 = CountySelection({"StateShortName" : "NJ", 
#                       "preference1" : "QualityofLife",
#                       "preference2":"HealthBehaviours",
#                       "preference3":"EconomicFactors",
#                       "preference4":"ClinicalCare"
#                     })

# s= p1.Selection()
# print(s)