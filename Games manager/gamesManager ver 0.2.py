import mysql.connector as sql
from mysql.connector import Error
import pandas as pd
import csv


gamesArray = []

def createServerConnection():
    try:
        connection = sql.connect(
            host="localHost",
            user="Grumbledore",
            passwd="password"
        )
        print("Connection established.")
    except Error as err:
        print("Error: ", err)

    return connection


def createDatabase(connection):
    cursor = connection.cursor()
    query = "CREATE DATABASE Games"
    try:
        cursor.execute(query)
        print("Success!")
    except Error as err:
        print("Error: ", err)


def executeQuery(connection, query):
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query)
        connection.commit()
        print("Query success!")
    except Error as err:
        print("Error: ", err)

def readQuery(connection, query):
    cursor = connection.cursor(buffered=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print("Error: ", err)

def createTable(connection):
    query = """CREATE TABLE games (
                Games_id INT NOT NULL AUTO_INCREMENT,
                Game VARCHAR(255) NOT NULL,
                Console VARCHAR (255) NOT NULL,
                PRIMARY KEY(Games_id)
                );
                """
    executeQuery(connection, query)


def connectDB():
    try:
        connection = sql.connect(
            host="localHost",
            user="Grumbledore",
            passwd="password",
            database="Games"

        )
        print("Connected to DB")
    except Error as err:
        print("Error: ", err)
    return connection

def readCSV(connection):
    query = "INSERT INTO games (Game, Console) VALUES\n"
    with open('gamesManager.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount != 0:
                gamesArray.append(row[0])
                gamesArray.append(row[1])
            lineCount+=1
    for i in range(0, (len(gamesArray)),2):
        if i != len(gamesArray)-2:
            string = "('{one}', '{two}'),\n".format(one = gamesArray[i].replace('\'', ''), two = gamesArray[i+1])
            query+= str(string)
        else:
            string = "('{one}', '{two}')".format(one = gamesArray[i].replace('\'', ''), two = gamesArray[i+1])
            query+= str(string)
    query+=";"
    print(query)
    executeQuery(connection, query)
    
def showAll():
    connection = connectDB()
    query = """
    SELECT *
    FROM games;
"""
    results = readQuery(connection, query)
    for result in results:
        print(result)
            
def searchGame(game):
    connection = connectDB()#While inefficient more user friendly
                            #So remove once the rest of the ui is user friendly
    query ="""
    SELECT * FROM games
    WHERE game LIKE \'%{name}%\';""".format(name = game)
    results = readQuery(connection, query)
    for result in results:
        print(result)

def searchConsole(console):
    connection = connectDB() #While inefficient more user friendly
                            #So remove once the rest of the ui is user friendly
    query ="""  
    SELECT * FROM games
    WHERE console LIKE \'%{name}%\';""".format(name = console)
    results = readQuery(connection, query)
    for result in results:
        print(result)

def addGame(gameName, console):
    connection = connectDB()#While inefficient more user friendly,
                            #So remove once the rest of the ui is user friendly
    query = """INSERT INTO Games (game, console)
                VALUES('{name}','{c}');""" .format(name=gameName,c = console)
    executeQuery(connection, query)

def Help():
    print("""You can type searchGame(game) {where game is a string}
            to search for games, for example typing "ze" will return
            games that contain ze so \"Legend of zelda\" etc
            searchConsole does the same thing with a console
            for example searchConsole(\"x\") will return xbox and xbox360 
            games
            You can also add a game by using addGame(gameName, console)""")


connection = createServerConnection()
connection = connectDB()
showAll()
print("Type Help() for help.")

