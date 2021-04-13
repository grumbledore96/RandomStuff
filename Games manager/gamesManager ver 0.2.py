import mysql.connector as sql
from mysql.connector import Error
import pandas as pd
import csv

connection = None
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
                Games_id INT PRIMARY KEY,
                Game VARCHAR(255) NOT NULL,
                Console VARCHAR (255) NOT NULL
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
    query = "INSERT INTO games VALUES\n"
    with open('gamesManager.csv', 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        lineCount = 0
        for row in csvReader:
            if lineCount != 0:
                gamesArray.append(row[0])
                gamesArray.append(row[1])
            lineCount+=1
    index = 0
    for i in range(0, (len(gamesArray)),2):
        if i != len(gamesArray)-2:
            string = "({indexx}, '{one}', '{two}'),\n".format(indexx = index, one = gamesArray[i].replace('\'', ''), two = gamesArray[i+1])
            query+= str(string)
            index+=1
        else:
            string = "({indexx}, '{one}', '{two}')".format(indexx = index, one = gamesArray[i].replace('\'', ''), two = gamesArray[i+1])
            query+= str(string)
            index+=1
    query+=";"
    print(query)
    
def showAll(connection):
    query = """
    SELECT *
    FROM games;
"""
    results = readQuery(connection, query)
    for result in results:
        print(result)
            



    

connection = createServerConnection()
connection = connectDB()
showAll(connection)

