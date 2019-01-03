#####
# Represents a property such as
# Park place or Mediterranean Avenue
#####

class Property:
    cost = 0 
    rent = 0 
    owner = -1 # 0 for player 1, 1 for player 2, etc 
    extra = 0
    mortgage = 0 
    name = ""
    color = -1

    def __init__(self, name, cost, rent, extra, mortgage, color):
        self.name = name
        self.cost = cost
        self.rent = rent
        self. extra = extra
        self.mortgage = mortgage
        self.color = color

    def canBePurchased(self, playerMoney):
        return playerMoney >= self.cost and self.owner == -1

    def canAffordToStay(self, playerMoney):
        return playerMoney > self.rent

    def getPropertyInfo(self):
        print(f"Owner: {self.name}, Cost: {self.cost}, Rent: {self.rent}, Owner:{self.owner}")

    # Check to see if player owns all properties of a given color
    # If so, charge double the rent
    def rentIfMonopoly(self, propertyList):
        # Get a subset of the properties of the same property in a given color.
        subList = list(filter(lambda x: x.color == self.color, propertyList))
        print(f"My sublist size is {len(subList)}")
        joinedList = ",".join(str(x.name) for x in subList)
        print(f"Properties in this color are {joinedList}")
        # Check to see in the sublist are owned by the same person
        uniqueListOfOwners = list(set(x.owner for x in subList))
        
        ownerList = ",".join(str(x) for x in uniqueListOfOwners)
        print(f"Owners are  {ownerList}")
        if(len(uniqueListOfOwners) == 1 and uniqueListOfOwners[0] != -1):
            return self.rent * 2
        else:
            return self.rent
        


    

#             1                   2                3                4                 5                   6                  7              8                   9               10                11                12              13          14              15              16              17                 18              19                        20                 21         22           23                   24                         25              26                
list1 = ["Mediterranean Ave.", "Baltic Ave.", "Oriental Ave.", "Vermont Ave.", "Connecticut Ave.", "St. Charles Place", "States Ave.", "Virginia Ave.","St. James Place", "Tennessee Ave.", "New York Ave.", "Kentucky Ave.","Indiana Ave.","Illinois Ave.","Atlantic Ave.","Ventnor Ave.", "Marvin Gardens", "Pacific Ave.", "North Carolina Ave.", "Pennsylvania Ave.","Park Place", "Boardwalk", "Reading Railroad", "Pennsylvania Railroad","B. & O. Railroad","Short Line Railroad","Electric Company","Water Works"]
#Cost of places
#         1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
list2 = [60,60,100,100,120,140,140,160,180,180,200,220,220,240,260,260,280,300,300,320,350,400,200,200,200,200,150,150]
#Owner of the place
#         1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26
list3 = [0, 0, 0,  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  , 0  ,0   ,0]
#Rent
#         1  2  3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26         
list4 = [2, 4, 6,  6  ,8  ,10 ,10 ,12 ,14 ,14 ,16 ,18 ,18 ,20 ,22 ,22 ,24 ,26 ,26 , 28,35 ,50 ,25 ,25 ,25 ,25 , 0   ,0]
#Extra
list5 = [0, 0, 0,  0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,0  ,  0,0  ,0  ,0  ,0  ,0  ,0 ,  0   ,0]
#Most likely need a mortgage value.
#Need to add waterworks and electric company to for loops once finish.

# Color grouping list
#                      0  1  2  3  4  5  6  7
#                      D  L     O     Y
#                               r     e  G
#                      B  B  P  a     l  r  B
#                      l  l  i  n  R  l  e  l
#                      u  u  n  g  e  o  e  u
#                      e  e  k  e  d  w  n  e
# Already was a monopoly represents the the grouping of properties. We use this to check for whether
# Or not a player owns all of the properties on a given color.
colorGrouping = [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9]


def createPropertyList():
    propertyList = []
    for value in range(len(list1)):
        propertyList.append(Property(list1[value], list2[value], list4[value], list5[value], 0, colorGrouping[value]))
    return propertyList

