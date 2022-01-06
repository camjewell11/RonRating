import mysql.connector
import pandas as pd
import config

# initialize database connection
def initializeDBConnection():
    try:
        myDB = mysql.connector.connect(
            host = config.host,
            user = config.user,
            password = config.password,
            database = config.db_name)
        cursor = myDB.cursor()
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    return myDB, cursor

def writeBeerToList(myDB, cursor, table, ID, name, type, abv, rating):
    query = ("INSERT INTO " + table + " (ID, `Beer Name`, `Beer Type`, ABV, Rating) "
            "VALUES (%s, %s, %s, %s, %s);")
    values = (ID, name, type, abv, rating)
    cursor.execute(query, values)
    myDB.commit()

def readAllDataFromDB(cursor, table):
    query = "SELECT * FROM " + table
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def readColDataFromDB(cursor, table, col, value):
    query = "SELECT * FROM " + table + " WHERE " + str(col) + "=" + str(value)
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# used to create table in provided DB
def createTableInDB(myDB, cursor, tableName):
    query = "CREATE TABLE " + tableName
    cursor.execute(query)
    myDB.commit()

def addColumnToTable(myDB, cursor, table, columnName, colDataType):
    query = "ALTER TABLE " + table + " ADD COLUMN " + columnName + " " + colDataType
    cursor.execute(query)
    myDB.commit()

def removeColumnFromTable(myDB, cursor, table, columnName):
    query = "ALTER TABLE " + table + " DROP COLUMN " + columnName
    cursor.execute(query)
    myDB.commit()

# used to select/switch between databases
def useDatabase(myDB, cursor, DB):
    query = "USE " + DB
    cursor.execute(query)
    myDB.commit()

# closes database instances
def wrapUp(myDB, cursor):
    cursor.close()
    myDB.close()

if __name__=="__main__":
    myDB, cursor = initializeDBConnection()
    useDatabase(myDB, cursor, "BeerRatings")
    # addColumnToTable(myDB, cursor, "BeerList", "Beer Name", config.stringType)
    # addColumnToTable(myDB, cursor, "BeerList", "Rating", config.doubleType)
    # writeBeerToList(myDB, cursor, "BeerList", 2, "Moonshot", "Stout", 10, 9)
    # readAllDataFromDB(myDB, cursor, "BeerList")
    # readColDataFromDB(myDB, cursor, "BeerList", 'ID', 2)
    wrapUp(myDB, cursor)