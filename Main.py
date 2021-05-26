import mysql.connector

# initialize database connection
myDB = mysql.connector.connect(
    host = "beezrbeerratings.c6r8l4machqa.us-east-2.rds.amazonaws.com",
    user = "admin",
    password = "109NSSquare")
cursor = myDB.cursor()

createQuery = "CREATE DATABASE BeerRatings"

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