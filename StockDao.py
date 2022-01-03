# Data Represenation Big Project
# Created By: Sheldon D'Souza - G00387857


import mysql.connector
from mysql.connector import cursor
import db1config as cfg 

# Py file to connect to the database and perform CRUD operations on the datbase
# mysql operations are perfromed throughout the workbook

class StockDao:
    db = ""
    def __init__(self):
        #connect to the database
        self.db = mysql.connector.connect(
            host = cfg.mysql['host'],
            user= cfg.mysql['username'],
            password = cfg.mysql['password'],
            database =cfg.mysql['database']
        )

    def create(self, stock):
        #create a new record within the database
        cursor = self.db.cursor()
        sql = "insert into stock_close (ID, SYMBOL, OPEN, CLOSE, VOLUME) values (%s,%s,%s,%s,%s)"
        values = [
            stock['ID'],
            stock['symbol'],
            stock['open'],
            stock['close'],
            stock['volume']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def addfromAPI(self, stock):
        #populate the database with the information received from the external API
        cursor = self.db.cursor()
        sql = "insert into stock_close (SYMBOL, OPEN, CLOSE, VOLUME) values (%s,%s,%s,%s)"
        values = [
            stock['symbol'],
            stock['open'],
            stock['close'],
            stock['volume']
        ]
        #print(values)
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    def getAll(self):
        #obtain all values from the database
        cursor = self.db.cursor()
        sql = 'select * from stock_close'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray

    def findById(self, ID):
        #find an item from the database based on it's ID
        cursor = self.db.cursor()
        sql = 'select * from stock_close where ID = %s'
        values = [ ID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
        

    def update(self, stock):
        #update a value in te database
       cursor = self.db.cursor()
       sql = "update stock_close set symbol = %s, open = %s, close = %s, volume = %s where ID = %s"
       values = [
           stock['symbol'],
           stock['open'],
           stock['close'],
           stock['volume'],
           stock['ID']

       ]
       cursor.execute(sql, values)
       self.db.commit()
       return stock

    def delete(self, ID):
        #delete an item in the database
       cursor = self.db.cursor()
       sql = 'delete from stock_close where ID = %s'
       values = [ ID ]
       cursor.execute(sql, values)
       self.db.commit()
       
       return {}



    def convertToDict(self, result):
        #helper function to convert into dictionary items for easier processing
        colnames = ['ID','symbol', 'open', 'close', 'volume']
        stock = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                stock[colName] = value
        return stock

stockDao = StockDao()