from pymongo import MongoClient
import pandas as pd


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
        # TBD Need to use aggregate function to optimize
        # aggregate([
        #              { $match: { status: "A" } },
        #              { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },
        #              { $sort: { total: -1 } }
        #            ])
        Counties = []
        for item in db.State.find({'StateShortName': self.StateShortName}): 
            for c in item['Counties']:
                StateLatitude = 0.0
                StateLongitude = 0.0
                if ( 'StateLatitude' in c['County']):
                    StateLatitude= float(c['County']['StateLatitude'])
                if ( 'StateLongitude' in c['County']):
                    StateLongitude= float(c['County']['StateLongitude'])       

                county = {  'StateName': item['StateName'],
                            'StateShortName' : self.StateShortName,
                            'CountyName'  : c['County']['CountyName'],
                            'TotalArea' : c['County']['TotalArea'],
                            'Population': c['County']['Population'],
                            'Latitude': float(c['County']['Latitude'][:-1].strip()[1:]),
                            'Longitude': float(c['County']['Longitude'][:-1].strip().replace('–', '-')),
                            'CountyWikiLink': c['County']['CountyWikiLink'],
                            'AggregatedValue' : float( c['County'] [self.Preference1]['Z-Score']) * 0.4 +
                                                float( c['County'] [self.Preference2]['Z-Score']) * 0.3 +
                                                float( c['County'] [self.Preference3]['Z-Score']) * 0.2 +
                                                float( c['County'] [self.Preference4]['Z-Score']) * 0.1,
                            "StateLatitude":StateLatitude,
                            "StateLongitude":StateLongitude                    
                        }
                # Add the county to the collection
                Counties.append(county) 
                
        # Populate the dataframe
        df = pd.DataFrame(Counties).reset_index(drop=True)
        print(df.keys())
        df= df.sort_values(by=['AggregatedValue'], ascending=[True] )
        top3 = df.head(3)

        return top3

p1 = CountySelection({"StateShortName" : "NJ", 
                      "preference1" : "QualityofLife",
                      "preference2":"HealthBehaviours",
                      "preference3":"EconomicFactors",
                      "preference4":"ClinicalCare"
                    })

s= p1.Selection()
print(s)
