class Buildings:
    def __init__(self, levels, constructionYear, location):
        self.levels = levels
        self.constructionYear = constructionYear
        self.location = location

    def buildNewLevel(self):
        self.levels = self.levels + 1

class House(Buildings):
    def __init__(self, levels, constructionYear, location, bedrooms, bathrooms):
        super().__init__(levels, constructionYear, location)
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

colpatriaTower = Buildings(49,1980,"San Diego")
colpatriaTower.buildNewLevel()
print(colpatriaTower.levels)

myHouse = House(4, 1995, "Suba", 12, 6)
myHouse.buildNewLevel()
print(myHouse.levels)