import makedict as md

#___________THIS IS THE CODE FOR THE ADDING OF PAINTINGS___________________________________________
def writer(type,price,sold):
    print(type,price,sold)
    text = "{}:{}:{}:\n".format(type,price,sold)
    print(text)
    with open("paintingHistory.txt","a") as f:
        f.write(text)
        f.close()


def choicePrice(paintingChoice):
    
    
    
        
    paintingOptions = md.getDict()
    
    paintingPrice = paintingOptions[paintingChoice]
    
    

    return paintingPrice

def choice(cost,paintType):
    print("ran")
    price = choicePrice(paintType)
    
   #-[ for i in paintingOptions:
   #      count+=1
   #      print("{}. {}, ${}".format(count,i,paintingOptions[i]))
    
    value = cost
    writer(paintType,price,value)
#______________________________________________________________________________________________________________________

#______________Paint Type Counts__________________________________________________________
def getCounts():
    paintingHistory = open('paintingHistory.txt',"r")
    lines = paintingHistory.readlines()
    MoodCount = 0
    FigureCount = 0
    SmallCount = 0
    MedCount = 0
    LrgCount = 0
    totalCount = 0
    for line in lines:
        totalCount+=1
        data = line.split(":")
        paintType = data[0]

        if paintType == "Mood Painting":
            MoodCount+=1
        elif paintType == "Figure Painting":
            FigureCount+=1
        elif paintType == "Small Painting":
            SmallCount+=1
        elif paintType == "Medium Painting":
            MedCount+=1
        elif paintType == "Large Painting":
            LrgCount+=1
    paintingHistory.close() 
    return FigureCount,SmallCount,MedCount,LrgCount,MoodCount
def printCounts(fgrcnt,smlcnt,medcnt,lrgcnt,mdcnt):
    typelist = fgrcnt,smlcnt,medcnt,lrgcnt,mdcnt
    options = md.getDict()
    count=0
    for i in options:
        
        print("{}: {}".format(i,typelist[count]))
        count+=1

def typeCount():
    mdcnt,fgrcnt,smlcnt,medcnt,lrgcnt = getCounts()
    printCounts(mdcnt,fgrcnt,smlcnt,medcnt,lrgcnt)

#____________________________________________________________________________________________________________--

#____________________Total Cost Code_______________________________________________
def getCosts():
    paintingHistory = open("paintingHistory.txt","r")
    lines = paintingHistory.readlines()
    totalCost = 0
    for line in lines:
        data = line.split(":")
        totalCost += int(data[1])
    return totalCost
def printCosts(totalCost):
    print("Total Costs: {}".format(totalCost))
def costCount():
    totalCost = getCosts()
    printCosts(totalCost)
#________________________________________________________________________________________

#____________________Total Sale Code_______________________________________________
def getSales():
    paintingHistory = open("paintingHistory.txt","r")
    lines = paintingHistory.readlines()
    totalSales = 0
    for line in lines:
        data = line.split(":")
        totalSales += int(data[2])
    return totalSales
def printsales(totalSales):
    print("Total Sales: {}".format(totalSales))
def saleCount():
    totalSales = getSales()
    printsales(totalSales)
#________________________________________________________________________________________

#________________Net Gain Code______________________________________________-
def getGain():
    paintingHistory = open("paintingHistory.txt","r")
    lines = paintingHistory.readlines()
    totalSales = 0
    totalCost= 0
    for line in lines:
        data = line.split(":")
        totalCost += int(data[1])
        totalSales += int(data[2])
    netGain = totalSales - totalCost
    
    return netGain
def printGain(netGain):
    print("Net Income: {}".format(netGain))
def gainCount():
    netGain = getGain()
    printGain(netGain)
#________________________________________________________________


#________________Net Gain Code______________________________________________-
def getBestSell():
    paintingHistory = open("paintingHistory.txt","r")
    lines = paintingHistory.readlines()
    bestSale = 0
    linecount = 1
    bestln=""
    for line in lines:
        data = line.split(":")
        if int(data[2])> bestSale:
            bestln = line
            bestSale = int(data[2])
        linecount+=1
        
    return bestSale,bestln
    
def bestSellPrint(bestSale,bestln):
    data = bestln.split(":")

    text = "{}: ${}".format(data[0],data[2])
    print(text)
def bestSell():
    bestSale,bestln = getBestSell()
    bestSellPrint(bestSale,bestln)
#________________________________________________________________


#_______________Main Menu Code___________________________________________________________________________________________-
def mainMenuHandler():
    selection = input("Please select the corresponding number to your choice: ")
    if int(selection) == 1:
     choice()
    if int(selection) == 2:
        typeCount()
    if int(selection) == 3:
        costCount()
    if int(selection) == 4:
        saleCount()
    if int(selection) == 5:
        gainCount()
    if int(selection) == 6:
        bestSell()
        

def mainMenu():
    menuOptions = ['Add Paintings',"Type Counts","Total Costs","Total Sales","Net Gain","Best Selling"]
    count = 0
    MainMenuText = "\x1B[4m" + "Main Menu" + "\x1B[0m"
    print(MainMenuText)
    for i in menuOptions:
        count+=1
        print("{}. {}".format(count,i))
    mainMenuHandler()
#________________________________________________________________________________________________________________________---


if __name__ == "__main__":
      mainMenu()




