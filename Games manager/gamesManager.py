import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 7)
pd.set_option('display.width', 1080)
class GamesManager:
    def __init__(self):
        self.dataFrame=""
        self.consoleListReader = open("consoles.txt", 'r')
        self.gamesListReader = open("games.txt", 'r') #Read files
        

        self.consoleList = (self.consoleListReader.read()).split(",")
        self.gamesListTemp = (self.gamesListReader.read()).split("\n")
        
        self.gamesList = [[""]]*len(self.consoleList)
        for i in range(len(self.gamesListTemp)):
            self.gamesList[i]=self.gamesListTemp[i].split(",") #splits everything properly

        for i in range(len(self.consoleList)):
            for j in range(len(self.gamesList[i])):
                self.gamesList[i][j]=self.gamesList[i][j].title()

        self.cleaner()

        
    def addConsole(self, console):
        self.consoleList.append(console)
        self.gamesList.append([])
        
    def addGame(self,gameName,console):
        consoleForGame = self.consoleList.index(console)
        print(consoleForGame)
        self.gamesList[consoleForGame].append(gameName.title())
        try:
            self.gamesList.remove("")
        except:
            print("")

    def showConsoles(self):
        print(self.consoleList)

    def showGames(self):
        print(self.gamesList)

    def cleaner(self):
        for i in range(len(self.consoleList)):
            self.gamesList[i] = list(filter(None, self.gamesList[i]))
        
    def viewList(self):
        self.cleaner()
        for i in range(len(self.consoleList)):
            self.gamesList[i]=sorted(self.gamesList[i])
        numbersArray=[]#for storeing the length of each array to find the max
        for i in range(len(self.consoleList)):
            numbersArray.append(len(self.gamesList[i]))

        maxNumber = max(numbersArray)
        
        for i in range(len(self.consoleList)):
            while len(self.gamesList[i]) != maxNumber: #Fills in the arrays so that the sections are all of equal size
                self.gamesList[i].append("")

        newArr = np.array(self.gamesList).T
        listDataFrame = pd.DataFrame(newArr,columns=self.consoleList)
        self.dataFrame=listDataFrame
        print(listDataFrame)

        
    def viewConsoleList(self, console): #might want this if lists get huge
        x = self.dataFrame[console]
        print(console + " Games:")
        print(x)
        
    def exit(self):
        self.cleaner()
        self.consoleListReader.close()
        self.gamesListReader.close()
        x = open("games.txt", 'w')
        y = open("consoles.txt", 'w')
        stringToWrite=""
        for i in range(len(self.gamesList)):
            stringToWrite=stringToWrite+self.gamesList[i][0]
            for j in range(1,len(self.gamesList[i])):
                stringToWrite=stringToWrite+","+self.gamesList[i][j]
            stringToWrite=stringToWrite+"\n"
        x.write(stringToWrite[:-1])
        y.write(",".join(map(str, self.consoleList)))
        x.close()
        y.close()
        backx = open("gamesBackUp.txt", 'w+')
        backy = open("consolesBackUp.txt", 'w+')
        backx.write(stringToWrite[:-1])
        backy.write(",".join(map(str, self.consoleList)))
        backx.close()
        backy.close()

gamesManager = GamesManager()
gamesManager.viewList()
