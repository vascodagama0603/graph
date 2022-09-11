from PyQt5.QtWidgets import *
import sqlite3
import pandas
import plotly.graph_objects as go
import plotly.express as px
import datetime
import pathlib
import os
from db import DB

class GraphSourse():
    def __init__(self):
        self.db_connect = None
        self.db_tablelist = []
        self.dbAxisList = []

    def setDbdata(self,dbpath):
        self.dbpath = dbpath
        self.db = DB(filename=self.dbpath, dbtype="sqlite")
        self.db_tablelist = [x.name for x in self.db.tables if not x.name == "sqlite_sequence"]

    def getStartTime(self):
        self.filter_sttime = datetime.datetime(2022,5,12,10,00)
        self.filter_endtime = datetime.datetime(2022,5,12,10,10)
        ##time filter
        self.df[self.xlabel] = pandas.to_datetime(self.df[self.xlabel])
        if self.filter_sttime:
            self.df = self.df[self.df[self.xlabel] >= self.filter_sttime]
        if self.filter_endtime:
            self.df = self.df[self.df[self.xlabel] <= self.filter_endtime]

    def getvalueFilter(self,minvals,maxvals):
        self.minvals = minvals.split(",")
        self.maxvals = maxvals.split(",")
        ##Value filter
        for i, l in enumerate(self.ylabel):
            self.df.loc[self.df[l] < self.minvals[i], l] = None
            self.df.loc[self.df[l] > self.maxvals[i], l] = None


    def getDataFrame(self):
        ylabel = ['v1', 'v2', 'v3']
        ySQLText = ', '.join(ylabel)

        self.df = pandas.read_sql('SELECT ' + self.xlabel + ' ,' + ySQLText + ' FROM ' + tblname, self.Dbcntn)

    def getAxisList(self,table):
        print("AAAAAAAAAA,",table)
        df = self.db.query("select * from " +table + ";")
        self.dbAxisList = df.columns.tolist()
        self.dbAxisList.append("")
        #self.df = pandas.read_sql('SELECT ' + self.xlabel + ' ,' + ySQLText + ' FROM ' + tblname, self.Dbcntn)