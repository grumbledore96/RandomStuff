# makes a csv file using 2 files
import csv

consoleListReader = open("consoles.txt", 'r')
gamesListReader = open("games.txt", 'r') #Read files

consoleList = (consoleListReader.read()).split(",")
gamesListTemp = (gamesListReader.read()).split("\n")

gamesList = [[""]]*len(consoleList)
for i in range(len(gamesListTemp)):
    gamesList[i]=gamesListTemp[i].split(",") #splits everything properly

for i in range(len(consoleList)):
    for j in range(len(gamesList[i])):
        gamesList[i][j]=gamesList[i][j].title()

with open('gamesManager.csv',mode='w+',newline='') as gamesManager:
    gamesManagerWriter = csv.writer(gamesManager, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(consoleList)):
        for j in range(len(gamesList[i])):
            gamesManagerWriter.writerow([gamesList[i][j], consoleList[i]])
