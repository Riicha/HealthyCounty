#-----------------Import Dependencies----------------------------# 
# import json
import pymongo
from pymongo import MongoClient
#--------------------------------------------------------------------------------#
def mongodbset():

        # Connection for local host
        conn = 'mongodb://localhost:27017'
        client = pymongo.MongoClient(conn)
        db=client.healthi_db
        
        #Connection for remote host
        # conn = 'mongodb://<dbuser>:<dbpassword>@ds255332.mlab.com:55332/healthi_db'
        # conn = 'mongodb://Riicha:mlabpolkA#1122@ds113873.mlab.com:13873/healthi_db'
        # client = pymongo.MongoClient(conn,ConnectTimeoutMS=30000)
        # db = client.get_default_database()
        
        Ranks = [
                    {
                        "State": "New York",
                        "FIPS": 36000,
                        "CountyDetails":
                        [
                            {
                            
                            "FIPS": 36001,
                            "County": "Albany",
                            "Z-Score": -0.55,
                            "Rank": 8
                            },
                            {
                            "FIPS": 36003,
                            "County": "Allegany",
                            "Z-Score": 0.34,
                            "Rank": 48
                            },
                            {
                            "FIPS": 36005,
                            "County": "Bronx",
                            "Z-Score": 1.43,
                            "Rank": 62
                            },
                            {
                            "FIPS": 36007,
                            "County": "Broome",
                            "Z-Score": 0.06,
                            "Rank": 34
                            },
                            {
                            "FIPS": 36009,
                            "County": "Cattaraugus",
                            "Z-Score": 0.55,
                            "Rank": 60
                            },
                            {
                            "FIPS": 36011,
                            "County": "Cayuga",
                            "Z-Score": 0.25,
                            "Rank": 43
                            },
                            {
                            "FIPS": 36013,
                            "County": "Chautauqua",
                            "Z-Score": 0.48,
                            "Rank": 57
                            },
                            {
                            "FIPS": 36015,
                            "County": "Chemung",
                            "Z-Score": 0.39,
                            "Rank": 53
                            },
                            {
                            "FIPS": 36017,
                            "County": "Chenango",
                            "Z-Score": 0.07,
                            "Rank": 35
                            },
                            {
                            "FIPS": 36019,
                            "County": "Clinton",
                            "Z-Score": 0.21,
                            "Rank": 42
                            },
                            {
                            "FIPS": 36021,
                            "County": "Columbia",
                            "Z-Score": -0.33,
                            "Rank": 13
                            },
                            {
                            "FIPS": 36023,
                            "County": "Cortland",
                            "Z-Score": 0.04,
                            "Rank": 32
                            },
                            {
                            "FIPS": 36025,
                            "County": "Delaware",
                            "Z-Score": 0.35,
                            "Rank": 49
                            },
                            {
                            "FIPS": 36027,
                            "County": "Dutchess",
                            "Z-Score": -0.53,
                            "Rank": 9
                            },
                            {
                            "FIPS": 36029,
                            "County": "Erie",
                            "Z-Score": 0.03,
                            "Rank": 31
                            },
                            {
                            "FIPS": 36031,
                            "County": "Essex",
                            "Z-Score": -0.15,
                            "Rank": 21
                            },
                            {
                            "FIPS": 36033,
                            "County": "Franklin",
                            "Z-Score": 0.52,
                            "Rank": 59
                            },
                            {
                            "FIPS": 36035,
                            "County": "Fulton",
                            "Z-Score": 0.41,
                            "Rank": 55
                            },
                            {
                            "FIPS": 36037,
                            "County": "Genesee",
                            "Z-Score": -0.09,
                            "Rank": 27
                            },
                            {
                            "FIPS": 36039,
                            "County": "Greene",
                            "Z-Score": 0.16,
                            "Rank": 39
                            },
                            {
                            "FIPS": 36041,
                            "County": "Hamilton",
                            "Z-Score": -0.15,
                            "Rank": 20
                            },
                            {
                            "FIPS": 36043,
                            "County": "Herkimer",
                            "Z-Score": 0.39,
                            "Rank": 54
                            },
                            {
                            "FIPS": 36045,
                            "County": "Jefferson",
                            "Z-Score": 0.33,
                            "Rank": 46
                            },
                            {
                            "FIPS": 36047,
                            "County": "Kings",
                            "Z-Score": 0.38,
                            "Rank": 52
                            },
                            {
                            "FIPS": 36049,
                            "County": "Lewis",
                            "Z-Score": 0.25,
                            "Rank": 44
                            },
                            {
                            "FIPS": 36051,
                            "County": "Livingston",
                            "Z-Score": -0.13,
                            "Rank": 25
                            },
                            {
                            "FIPS": 36053,
                            "County": "Madison",
                            "Z-Score": -0.13,
                            "Rank": 23
                            },
                            {
                            "FIPS": 36055,
                            "County": "Monroe",
                            "Z-Score": -0.13,
                            "Rank": 22
                            },
                            {
                            "FIPS": 36057,
                            "County": "Montgomery",
                            "Z-Score": 0.52,
                            "Rank": 58
                            },
                            {
                            "FIPS": 36059,
                            "County": "Nassau",
                            "Z-Score": -1.17,
                            "Rank": 1
                            },
                            {
                            "FIPS": 36061,
                            "County": "New York",
                            "Z-Score": -0.34,
                            "Rank": 12
                            },
                            {
                            "FIPS": 36063,
                            "County": "Niagara",
                            "Z-Score": 0.37,
                            "Rank": 51
                            },
                            {
                            "FIPS": 36065,
                            "County": "Oneida",
                            "Z-Score": 0.19,
                            "Rank": 41
                            },
                            {
                            "FIPS": 36067,
                            "County": "Onondaga",
                            "Z-Score": -0.23,
                            "Rank": 15
                            },
                            {
                            "FIPS": 36069,
                            "County": "Ontario",
                            "Z-Score": -0.38,
                            "Rank": 11
                            },
                            {
                            "FIPS": 36071,
                            "County": "Orange",
                            "Z-Score": -0.21,
                            "Rank": 17
                            },
                            {
                            "FIPS": 36073,
                            "County": "Orleans",
                            "Z-Score": 0.47,
                            "Rank": 56
                            },
                            {
                            "FIPS": 36075,
                            "County": "Oswego",
                            "Z-Score": 0.61,
                            "Rank": 61
                            },
                            {
                            "FIPS": 36077,
                            "County": "Otsego",
                            "Z-Score": -0.21,
                            "Rank": 18
                            },
                            {
                            "FIPS": 36079,
                            "County": "Putnam",
                            "Z-Score": -0.82,
                            "Rank": 4
                            },
                            {
                            "FIPS": 36081,
                            "County": "Queens",
                            "Z-Score": -0.02,
                            "Rank": 28
                            },
                            {
                            "FIPS": 36083,
                            "County": "Rensselaer",
                            "Z-Score": -0.29,
                            "Rank": 14
                            },
                            {
                            "FIPS": 36085,
                            "County": "Richmond",
                            "Z-Score": -0.13,
                            "Rank": 24
                            },
                            {
                            "FIPS": 36087,
                            "County": "Rockland",
                            "Z-Score": -0.6,
                            "Rank": 6
                            },
                            {
                            "FIPS": 36089,
                            "County": "St. Lawrence",
                            "Z-Score": 0.35,
                            "Rank": 50
                            },
                            {
                            "FIPS": 36091,
                            "County": "Saratoga",
                            "Z-Score": -0.84,
                            "Rank": 2
                            },
                            {
                            "FIPS": 36093,
                            "County": "Schenectady",
                            "Z-Score": -0.18,
                            "Rank": 19
                            },
                            {
                            "FIPS": 36095,
                            "County": "Schoharie",
                            "Z-Score": 0.02,
                            "Rank": 30
                            },
                            {
                            "FIPS": 36097,
                            "County": "Schuyler",
                            "Z-Score": 0.31,
                            "Rank": 45
                            },
                            {
                            "FIPS": 36099,
                            "County": "Seneca",
                            "Z-Score": 0.15,
                            "Rank": 37
                            },
                            {
                            "FIPS": 36101,
                            "County": "Steuben",
                            "Z-Score": 0.16,
                            "Rank": 38
                            },
                            {
                            "FIPS": 36103,
                            "County": "Suffolk",
                            "Z-Score": -0.58,
                            "Rank": 7
                            },
                            {
                            "FIPS": 36105,
                            "County": "Sullivan",
                            "Z-Score": 0.33,
                            "Rank": 47
                            },
                            {
                            "FIPS": 36107,
                            "County": "Tioga",
                            "Z-Score": -0.1,
                            "Rank": 26
                            },
                            {
                            "FIPS": 36109,
                            "County": "Tompkins",
                            "Z-Score": -0.76,
                            "Rank": 5
                            },
                            {
                            "FIPS": 36111,
                            "County": "Ulster",
                            "Z-Score": -0.22,
                            "Rank": 16
                            },
                            {
                            "FIPS": 36113,
                            "County": "Warren",
                            "Z-Score": -0.41,
                            "Rank": 10
                            },
                            {
                            "FIPS": 36115,
                            "County": "Washington",
                            "Z-Score": 0.04,
                            "Rank": 33
                            },
                            {
                            "FIPS": 36117,
                            "County": "Wayne",
                            "Z-Score": 0.17,
                            "Rank": 40
                            },
                            {
                            "FIPS": 36119,
                            "County": "Westchester",
                            "Z-Score": -0.82,
                            "Rank": 3
                            },
                            {
                            "FIPS": 36121,
                            "County": "Wyoming",
                            "Z-Score": 0.15,
                            "Rank": 36
                            },
                            {
                            "FIPS": 36123,
                            "County": "Yates",
                            "Z-Score": 0.01,
                            "Rank": 29
                            }
                        ]
                    },
                    {
                    "State": "New Jersey",
                    "FIPS": 34000,
                    "CountyDetails":
                        [
                            {
                            "FIPS": 34001,
                            "County": "Atlantic",
                            "Z-Score": 0.7,
                            "Rank": 19
                            },
                            {
                            "FIPS": 34003,
                            "County": "Bergen",
                            "Z-Score": -0.76,
                            "Rank": 4
                            },
                            {
                            "FIPS": 34005,
                            "County": "Burlington",
                            "Z-Score": -0.31,
                            "Rank": 8
                            },
                            {
                            "FIPS": 34007,
                            "County": "Camden",
                            "Z-Score": 0.45,
                            "Rank": 15
                            },
                            {
                            "FIPS": 34009,
                            "County": "Cape May",
                            "Z-Score": 0.39,
                            "Rank": 14
                            },
                            {
                            "FIPS": 34011,
                            "County": "Cumberland",
                            "Z-Score": 1.26,
                            "Rank": 21
                            },
                            {
                            "FIPS": 34013,
                            "County": "Essex",
                            "Z-Score": 0.6,
                            "Rank": 17
                            },
                            {
                            "FIPS": 34015,
                            "County": "Gloucester",
                            "Z-Score": 0.17,
                            "Rank": 13
                            },
                            {
                            "FIPS": 34017,
                            "County": "Hudson",
                            "Z-Score": 0.49,
                            "Rank": 16
                            },
                            {
                            "FIPS": 34019,
                            "County": "Hunterdon",
                            "Z-Score": -1.03,
                            "Rank": 1
                            },
                            {
                            "FIPS": 34021,
                            "County": "Mercer",
                            "Z-Score": -0.25,
                            "Rank": 9
                            },
                            {
                            "FIPS": 34023,
                            "County": "Middlesex",
                            "Z-Score": -0.33,
                            "Rank": 6
                            },
                            {
                            "FIPS": 34025,
                            "County": "Monmouth",
                            "Z-Score": -0.42,
                            "Rank": 5
                            },
                            {
                            "FIPS": 34027,
                            "County": "Morris",
                            "Z-Score": -0.93,
                            "Rank": 3
                            },
                            {
                            "FIPS": 34029,
                            "County": "Ocean",
                            "Z-Score": -0.04,
                            "Rank": 12
                            },
                            {
                            "FIPS": 34031,
                            "County": "Passaic",
                            "Z-Score": 0.64,
                            "Rank": 18
                            },
                            {
                            "FIPS": 34033,
                            "County": "Salem",
                            "Z-Score": 0.8,
                            "Rank": 20
                            },
                            {
                            "FIPS": 34035,
                            "County": "Somerset",
                            "Z-Score": -0.97,
                            "Rank": 2
                            },
                            {
                            "FIPS": 34037,
                            "County": "Sussex",
                            "Z-Score": -0.32,
                            "Rank": 7
                            },
                            {
                            "FIPS": 34039,
                            "County": "Union",
                            "Z-Score": -0.06,
                            "Rank": 11
                            },
                            {
                            "FIPS": 34041,
                            "County": "Warren",
                            "Z-Score": -0.07,
                            "Rank": 10
                            }
                        ]
                    },
                    {
                    "State": "Connecticut",
                    "FIPS": "09000",
                    "CountyDetails":
                    [ 
                        {
                        "FIPS": "09001",
                        "County": "Fairfield",
                        "Z-Score": -0.31,
                        "Rank": 4
                        },
                        {
                        "FIPS": "09003",
                        "County": "Hartford",
                        "Z-Score": 0.19,
                        "Rank": 5
                        },
                        {
                        "FIPS": "09005",
                        "County": "Litchfield",
                        "Z-Score": -0.33,
                        "Rank": 3
                        },
                        {
                        "FIPS": "09007",
                        "County": "Middlesex",
                        "Z-Score": -0.78,
                        "Rank": 1
                        },
                        {
                        "FIPS": "09009",
                        "County": "New Haven",
                        "Z-Score": 0.59,
                        "Rank": 7
                        },
                        {
                        "FIPS": "09011",
                        "County": "New London",
                        "Z-Score": 0.3,
                        "Rank": 6
                        },
                        {
                        "FIPS": "09013",
                        "County": "Tolland",
                        "Z-Score": -0.43,
                        "Rank": 2
                        },
                        {
                        "FIPS": "09015",
                        "County": "Windham",
                        "Z-Score": 0.77,
                        "Rank": 8
                        }
                    ]  
                    },
                    {
                    "State": "California",
                    "FIPS": "06000",
                    "CountyDetails":
                        [
                            {
                            "FIPS": "06001",
                            "County": "Alameda",
                            "Z-Score": -0.61,
                            "Rank": 9
                            },
                            {
                            "FIPS": "06003",
                            "County": "Alpine",
                            "Z-Score": "",
                            "Rank": "NR"
                            },
                            {
                            "FIPS": "06005",
                            "County": "Amador",
                            "Z-Score": -0.34,
                            "Rank": 18
                            },
                            {
                            "FIPS": "06007",
                            "County": "Butte",
                            "Z-Score": 0.1,
                            "Rank": 32
                            },
                            {
                            "FIPS": "06009",
                            "County": "Calaveras",
                            "Z-Score": -0.18,
                            "Rank": 22
                            },
                            {
                            "FIPS": "06011",
                            "County": "Colusa",
                            "Z-Score": 0.19,
                            "Rank": 37
                            },
                            {
                            "FIPS": "06013",
                            "County": "Contra Costa",
                            "Z-Score": -0.61,
                            "Rank": 8
                            },
                            {
                            "FIPS": "06015",
                            "County": "Del Norte",
                            "Z-Score": 0.61,
                            "Rank": 49
                            },
                            {
                            "FIPS": "06017",
                            "County": "El Dorado",
                            "Z-Score": -0.61,
                            "Rank": 7
                            },
                            {
                            "FIPS": "06019",
                            "County": "Fresno",
                            "Z-Score": 0.69,
                            "Rank": 53
                            },
                            {
                            "FIPS": "06021",
                            "County": "Glenn",
                            "Z-Score": 0.45,
                            "Rank": 45
                            },
                            {
                            "FIPS": "06023",
                            "County": "Humboldt",
                            "Z-Score": 0.08,
                            "Rank": 30
                            },
                            {
                            "FIPS": "06025",
                            "County": "Imperial",
                            "Z-Score": 1.05,
                            "Rank": 56
                            },
                            {
                            "FIPS": "06027",
                            "County": "Inyo",
                            "Z-Score": -0.02,
                            "Rank": 25
                            },
                            {
                            "FIPS": "06029",
                            "County": "Kern",
                            "Z-Score": 1.06,
                            "Rank": 57
                            },
                            {
                            "FIPS": "06031",
                            "County": "Kings",
                            "Z-Score": 0.59,
                            "Rank": 48
                            },
                            {
                            "FIPS": "06033",
                            "County": "Lake",
                            "Z-Score": 0.68,
                            "Rank": 52
                            },
                            {
                            "FIPS": "06035",
                            "County": "Lassen",
                            "Z-Score": 0.34,
                            "Rank": 42
                            },
                            {
                            "FIPS": "06037",
                            "County": "Los Angeles",
                            "Z-Score": 0.11,
                            "Rank": 34
                            },
                            {
                            "FIPS": "06039",
                            "County": "Madera",
                            "Z-Score": 0.67,
                            "Rank": 51
                            },
                            {
                            "FIPS": "06041",
                            "County": "Marin",
                            "Z-Score": -1.14,
                            "Rank": 1
                            },
                            {
                            "FIPS": "06043",
                            "County": "Mariposa",
                            "Z-Score": 0.05,
                            "Rank": 28
                            },
                            {
                            "FIPS": "06045",
                            "County": "Mendocino",
                            "Z-Score": 0.22,
                            "Rank": 38
                            },
                            {
                            "FIPS": "06047",
                            "County": "Merced",
                            "Z-Score": 0.72,
                            "Rank": 54
                            },
                            {
                            "FIPS": "06049",
                            "County": "Modoc",
                            "Z-Score": 0.14,
                            "Rank": 35
                            },
                            {
                            "FIPS": "06051",
                            "County": "Mono",
                            "Z-Score": -0.18,
                            "Rank": 21
                            },
                            {
                            "FIPS": "06053",
                            "County": "Monterey",
                            "Z-Score": 0.08,
                            "Rank": 31
                            },
                            {
                            "FIPS": "06055",
                            "County": "Napa",
                            "Z-Score": -0.48,
                            "Rank": 12
                            },
                            {
                            "FIPS": "06057",
                            "County": "Nevada",
                            "Z-Score": -0.41,
                            "Rank": 15
                            },
                            {
                            "FIPS": "06059",
                            "County": "Orange",
                            "Z-Score": -0.65,
                            "Rank": 6
                            },
                            {
                            "FIPS": "06061",
                            "County": "Placer",
                            "Z-Score": -0.96,
                            "Rank": 3
                            },
                            {
                            "FIPS": "06063",
                            "County": "Plumas",
                            "Z-Score": 0.06,
                            "Rank": 29
                            },
                            {
                            "FIPS": "06065",
                            "County": "Riverside",
                            "Z-Score": 0.24,
                            "Rank": 39
                            },
                            {
                            "FIPS": "06067",
                            "County": "Sacramento",
                            "Z-Score": 0.04,
                            "Rank": 27
                            },
                            {
                            "FIPS": "06069",
                            "County": "San Benito",
                            "Z-Score": -0.08,
                            "Rank": 24
                            },
                            {
                            "FIPS": "06071",
                            "County": "San Bernardino",
                            "Z-Score": 0.44,
                            "Rank": 44
                            },
                            {
                            "FIPS": "06073",
                            "County": "San Diego",
                            "Z-Score": -0.26,
                            "Rank": 20
                            },
                            {
                            "FIPS": "06075",
                            "County": "San Francisco",
                            "Z-Score": -0.73,
                            "Rank": 5
                            },
                            {
                            "FIPS": "06077",
                            "County": "San Joaquin",
                            "Z-Score": 0.35,
                            "Rank": 43
                            },
                            {
                            "FIPS": "06079",
                            "County": "San Luis Obispo",
                            "Z-Score": -0.58,
                            "Rank": 10
                            },
                            {
                            "FIPS": "06081",
                            "County": "San Mateo",
                            "Z-Score": -1.04,
                            "Rank": 2
                            },
                            {
                            "FIPS": "06083",
                            "County": "Santa Barbara",
                            "Z-Score": -0.34,
                            "Rank": 17
                            },
                            {
                            "FIPS": "06085",
                            "County": "Santa Clara",
                            "Z-Score": -0.95,
                            "Rank": 4
                            },
                            {
                            "FIPS": "06087",
                            "County": "Santa Cruz",
                            "Z-Score": -0.45,
                            "Rank": 13
                            },
                            {
                            "FIPS": "06089",
                            "County": "Shasta",
                            "Z-Score": 0.16,
                            "Rank": 36
                            },
                            {
                            "FIPS": "06091",
                            "County": "Sierra",
                            "Z-Score": 0,
                            "Rank": 26
                            },
                            {
                            "FIPS": "06093",
                            "County": "Siskiyou",
                            "Z-Score": 0.11,
                            "Rank": 33
                            },
                            {
                            "FIPS": "06095",
                            "County": "Solano",
                            "Z-Score": -0.11,
                            "Rank": 23
                            },
                            {
                            "FIPS": "06097",
                            "County": "Sonoma",
                            "Z-Score": -0.54,
                            "Rank": 11
                            },
                            {
                            "FIPS": "06099",
                            "County": "Stanislaus",
                            "Z-Score": 0.33,
                            "Rank": 41
                            },
                            {
                            "FIPS": "06101",
                            "County": "Sutter",
                            "Z-Score": 0.26,
                            "Rank": 40
                            },
                            {
                            "FIPS": "06103",
                            "County": "Tehama",
                            "Z-Score": 0.49,
                            "Rank": 47
                            },
                            {
                            "FIPS": "06105",
                            "County": "Trinity",
                            "Z-Score": 0.48,
                            "Rank": 46
                            },
                            {
                            "FIPS": "06107",
                            "County": "Tulare",
                            "Z-Score": 1.02,
                            "Rank": 55
                            },
                            {
                            "FIPS": "06109",
                            "County": "Tuolumne",
                            "Z-Score": -0.31,
                            "Rank": 19
                            },
                            {
                            "FIPS": "06111",
                            "County": "Ventura",
                            "Z-Score": -0.41,
                            "Rank": 16
                            },
                            {
                            "FIPS": "06113",
                            "County": "Yolo",
                            "Z-Score": -0.44,
                            "Rank": 14
                            },
                            {
                            "FIPS": "06115",
                            "County": "Yuba",
                            "Z-Score": 0.64,
                            "Rank": 50
                            }
                        ]
                        },
                        {
                        "State": "Alaska",
                        "FIPS": "02000",
                        "CountyDetails":
                            [
                                {
                                "FIPS": "02013",
                                "County": "Aleutians East",
                                "Z-Score": 0.0,
                                "Rank": 0
                                },
                                {
                                "FIPS": "02016",
                                "County": "Aleutians West",
                                "Z-Score": -0.35,
                                "Rank": 9
                                },
                                {
                                "FIPS": "02020",
                                "County": "Anchorage",
                                "Z-Score": -0.64,
                                "Rank": 2
                                },
                                {
                                "FIPS": "02050",
                                "County": "Bethel",
                                "Z-Score": 0.8,
                                "Rank": 23
                                },
                                {
                                "FIPS": "02060",
                                "County": "Bristol Bay",
                                "Z-Score": -0.08,
                                "Rank": 15
                                },
                                {
                                "FIPS": "02068",
                                "County": "Denali",
                                "Z-Score": -0.44,
                                "Rank": 7
                                },
                                {
                                "FIPS": "02070",
                                "County": "Dillingham",
                                "Z-Score": 0.46,
                                "Rank": 19
                                },
                                {
                                "FIPS": "02090",
                                "County": "Fairbanks North Star",
                                "Z-Score": -0.48,
                                "Rank": 6
                                },
                                {
                                "FIPS": "02100",
                                "County": "Haines",
                                "Z-Score": -0.51,
                                "Rank": 5
                                },
                                {
                                "FIPS": "02105",
                                "County": "Hoonah-Angoon",
                                "Z-Score": 0.19,
                                "Rank": 17
                                },
                                {
                                "FIPS": "02110",
                                "County": "Juneau",
                                "Z-Score": -0.75,
                                "Rank": 1
                                },
                                {
                                "FIPS": "02122",
                                "County": "Kenai Peninsula",
                                "Z-Score": -0.32,
                                "Rank": 10
                                },
                                {
                                "FIPS": "02130",
                                "County": "Ketchikan Gateway",
                                "Z-Score": -0.26,
                                "Rank": 12
                                },
                                {
                                "FIPS": "02150",
                                "County": "Kodiak Island",
                                "Z-Score": -0.58,
                                "Rank": 4
                                },
                                {
                                "FIPS": "02158",
                                "County": "Kusilvak",
                                "Z-Score": 1.11,
                                "Rank": 25
                                },
                                {
                                "FIPS": "02164",
                                "County": "Lake and Peninsula",
                                "Z-Score": 0.51,
                                "Rank": 20
                                },
                                {
                                "FIPS": "02170",
                                "County": "Matanuska-Susitna",
                                "Z-Score": -0.26,
                                "Rank": 13
                                },
                                {
                                "FIPS": "02180",
                                "County": "Nome",
                                "Z-Score": 0.64,
                                "Rank": 21
                                },
                                {
                                "FIPS": "02185",
                                "County": "North Slope",
                                "Z-Score": 0.45,
                                "Rank": 18
                                },
                                {
                                "FIPS": "02188",
                                "County": "Northwest Arctic",
                                "Z-Score": 0.91,
                                "Rank": 24
                                },
                                {
                                "FIPS": "02195",
                                "County": "Petersburg",
                                "Z-Score": -0.35,
                                "Rank": 8
                                },
                                {
                                "FIPS": "02198",
                                "County": "Prince of Wales-Hyder",
                                "Z-Score": 0.19,
                                "Rank": 16
                                },
                                {
                                "FIPS": "02220",
                                "County": "Sitka",
                                "Z-Score": -0.59,
                                "Rank": 3
                                },
                                {
                                "FIPS": "02230",
                                "County": "Skagway",
                                "Z-Score": 0.0,
                                "Rank": 0
                                },
                                {
                                "FIPS": "02240",
                                "County": "Southeast Fairbanks",
                                "Z-Score": -0.16,
                                "Rank": 14
                                },
                                {
                                "FIPS": "02261",
                                "County": "Valdez-Cordova",
                                "Z-Score": -0.27,
                                "Rank": 11
                                },
                                {
                                "FIPS": "02275",
                                "County": "Wrangell",
                                "Z-Score": 0.0,
                                "Rank": 0
                                },
                                {
                                "FIPS": "02282",
                                "County": "Yakutat",
                                "Z-Score": 0.0,
                                "Rank": 0
                                },
                                {
                                "FIPS": "02290",
                                "County": "Yukon-Koyukuk",
                                "Z-Score": 0.79,
                                "Rank": 22
                                }
                                ]
                        } 
                ]      
        #drop/create collection CR.
        db.CountyRanksZscores.drop()
        #insert into CountyRanksZscores collection
        result = db.CountyRanksZscores.insert_many(Ranks)
        # print("Multiple States {0}".format(result.inserted_ids))        

mongodbset()
