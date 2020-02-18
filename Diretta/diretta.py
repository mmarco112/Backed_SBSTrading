from selenium import webdriver
import unittest, time, re
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
import re
from utils import *


def Diretta_stat():
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-extensions")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-notifications");

    driver = webdriver.Chrome(executable_path= r"C:\Users\marco\Desktop\chromedriver.exe", options=options)

    driver.get('https://www.diretta.it/serie-a/')
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html)

    EventTime = []
    SquadraCasa = []
    SquadraTrasferta = []
    Partita = []

    for x in soup.find_all('div', {'class': 'summary-fixtures'}):
        for eventTime in x.find_all('div', {'class': 'event__time'}):
            EventTime.append(eventTime.text)
        for squadracasa in x.find_all('div', {'class': 'event__participant--home'}):
            SquadraCasa.append(squadracasa.text)
        for squadratrasferta in x.find_all('div', {'class': 'event__participant--away'}):
            SquadraTrasferta.append(squadratrasferta.text)

    for a, b  in zip(SquadraCasa, SquadraTrasferta):
        squadracasa = a 
        squadratrasferta = b
        partita = squadracasa + ' - ' + squadratrasferta
        Partita.append(partita)

    # print(EventTime)
    # print(SquadraCasa)
    # print(SquadraTrasferta)
    # print(Partita)

    client = MongoClient("mongodb://marco:Arkaton11!@cluster0-shard-00-00-7vwyj.mongodb.net:27017,cluster0-shard-00-01-7vwyj.mongodb.net:27017,cluster0-shard-00-02-7vwyj.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

    my_database = client.Diretta
    Collection = my_database.DatiSerieA
    Collection.remove()

    for a, b, c, d  in zip(Partita, EventTime, SquadraCasa, SquadraTrasferta):
        Diretta_dati = { 
        "Partita": a,
        'OraPartita' : b,
        'SquadraCasa' : c,
        'SquadraTrasferta' : d,
        'Update' : now(),
        }
        Collection.insert(Diretta_dati);