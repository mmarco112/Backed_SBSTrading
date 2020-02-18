from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
import unittest, time, re
# from selenium.common.exceptions import NoSuchElementException
import time
import os
import datetime
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from datetime import date
from random import randint
from pprint import pprint
import shutil
import glob
import requests
import sys
import unicodedata as ud
import codecs
from pymongo import MongoClient
from pprint import pprint
import pymongo
import time
from pymongo import MongoClient
import itertools

def Betfair_Eng():
  # Connessione al cluster
  client = MongoClient("mongodb://marco:Arkaton11!@cluster0-shard-00-00-7vwyj.mongodb.net:27017,cluster0-shard-00-01-7vwyj.mongodb.net:27017,cluster0-shard-00-02-7vwyj.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
  # Connessione al db Diretta e collection Calendario_SerieA
  db_diretta = client.Diretta
  collection_diretta = db_diretta.Calendario_SerieA
  # Connessione al db Betfair_ENG e collection Vincente
  db_betfair = client.Betfair_ENG
  collection_betfair = db_betfair.Vincente

  # Tutte le partite del calendario Diretta
  AllDiretta = []
  for x in collection_diretta.find():
    Partita = x.get('Partita')
    AllDiretta.append(Partita)

  #Tutte le partite del db Betfair_ENG
  VecchioBetfair = []
  for x in collection_betfair.find():
    Partita = x.get('Partita')
    VecchioBetfair.append(Partita)

 #Tutte le partite in calendario che sono all'interno di Betfair_ENG
  AllBetfair = []
  for i in AllDiretta:
    myquery ={ "Partita": i }
    mydoc = collection_betfair.find_one(myquery)
    AllBetfair.append(mydoc)

  BetfairFiltrate = [x for x in AllBetfair if x is not None]

  return BetfairFiltrate



Betfair_Eng()