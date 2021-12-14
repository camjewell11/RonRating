import mysql.connector
import pandas as pd
import config

import boto3

# initialize database connection
session = boto3.Session(profile_name='default')
client = session.client('rds')
token = client.generate_db_auth_token(DBHostname=config.host, Port=config.port, DBUsername=config.user, Region=config.region)

myDB = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.password,
    port = config.port,
    database = config.db_name)
cursor = myDB.cursor()

createQuery = "CREATE DATABASE BeerRatings"

def readConfig():
    df = pd.read_csv('')

def writeDataToDB(myDB):
    query = ("INSERT INTO BeerList (Beer Name, Beer Type, Rating) "
            "VALUES (Puddin' Pop, Stout, 10)")

    cursor = myDB.cursor()
    cursor.execute(query)
    myDB.commit()

def readDataFromDB(myDB):
    query = "SELECT TOP 3 name, sample FROM beezrbeerratings;"

    cursor.execute(query)
    myDB.commit()

# used to create table in provided DB
def createTableInDB(tableName):
    query = "CREATE TABLE " + tableName

    cursor.execute(query)
    myDB.commit()

def addColumnToTable(table, columnName):
    query = "ALTER TABLE " + table + " ADD " + columnName
    cursor.execute(query)
    myDB.commit()

def removeColumnFromTable(table, columnName):
    query = "ALTER TABLE " + table + " ADD " + columnName
    cursor.execute(query)
    myDB.commit()

# used to select/switch between databases
def useDatabase(DB):
    query = "USE " + DB

    cursor.execute(query)
    myDB.commit()

# closes database instances
def wrapUp():
    cursor.close()
    myDB.close()

if __name__=="__main__":
    useDatabase("BeerRatings")
    addColumnToTable("BeerRatings", "Beer Name")
    addColumnToTable("BeerRatings", "Beer Type")
    addColumnToTable("BeerRatings", "Rating")
    writeDataToDB(myDB)
    readDataFromDB(myDB)
    wrapUp()