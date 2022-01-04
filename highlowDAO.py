# Data Represenation Big Project
# Created By: Sheldon D'Souza - G00387857

import mysql.connector
from mysql.connector import cursor
import db2config as cfg #import database config file.

# The purpose of creating a separate py file is to connect to the second database which records the highs and lows for a patricular stock
# There is a separate class and functions defined to deal with populating this database.
# See StockDAO for documentation.

class HighLowDao:
    #connect to the database
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user= cfg.mysql['username'],
            password = cfg.mysql['password'],
            database =cfg.mysql['database']
        )


    #update the fields in the database with the values received from the API
    def highLowsAPI(self, stock):
        cursor = self.db.cursor()
        sql = "insert into high_low (SYMBOL, HIGH, LOW) values (%s,%s,%s)"
        values = [
            stock['symbol'],
            stock['high'],
            stock['low'],
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        #obtain all values from the database
        cursor = self.db.cursor()
        sql = 'select * from high_low'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def delete(self, ID):
        #delete an item in the database
       cursor = self.db.cursor()
       sql = 'delete from high_low where ID = %s'
       values = [ ID ]
       cursor.execute(sql, values)
       self.db.commit()
       
       return {}


    def convertToDict(self, result):
        colnames = ['ID','symbol', 'high', 'low']
        stock = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                stock[colName] = value
        return stock

highlowDao = HighLowDao()