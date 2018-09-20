class County:
    def __init__(self, countyData):
        self.StateShortName = countyData['StateShortName']
        # self.StateName = countyData['StateName']
        self.CountyName = countyData['CountyName']
        self.TotalArea = countyData['TotalArea']
        self.Population = countyData['Population']
        self.Latitude = countyData['Latitude']
        self.Longitude = countyData['Longitude']
        self.CountyWikiLink = countyData['CountyWikiLink']


