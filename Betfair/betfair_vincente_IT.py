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
from utils import *
from configuration import *





def betfair_vincente_IT():
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-extensions")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-notifications");

    driver = webdriver.Chrome(executable_path= Path_ChromeDriver, options=options)



    driver.get('https://www.betfair.it/sport/football')
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html)
    SerieA = soup.find('a', {'title': 'Italia - Serie A'})
    hrefSerieA = SerieA['href']
    driver.get('https://www.betfair.it' + str(hrefSerieA))
    html = driver.page_source
    soup = BeautifulSoup(html)
    StartingIn = []
    Partita = []
    SquadraCasa = []
    SquadraTrasferta = []
    V1 = []
    X = []
    V2 = []
    for ultag in soup.find_all('ul', {'class': 'event-list'}):
        for lidate in ultag.find_all('span', {'class': 'event-status-container'}):
            InizioIn = lidate.text
            StartingIn.append(InizioIn.replace('\n',''))
        for liPartita in ultag.find_all('div', {'class': 'teams-container'}):
            Match = liPartita.text
            Match.replace('\n',' ')
            splitted = Match.split()     
            TuttalaPartita = splitted[0] + ' - ' + splitted[1]
            SquadraCasa.append(splitted[0])
            SquadraTrasferta.append(splitted[1])
            Partita.append(TuttalaPartita)
        for liX1 in ultag.find_all('div', {'class': 'market-3-runners'}):
            x1 = liX1.text
            x1Clean = x1.replace('\n',' ')
            splitted = x1Clean.split()
            _1_ = splitted[0]
            _X_ = splitted[1]
            _2_= splitted[2]
            V1.append(_1_)
            X.append(_X_)
            V2.append(_2_)

    # print(StartingIn)
    # print(Partita)
    # print(V1)
    # print(X)
    # print(V2)

    client = MongoClient(connectionString)

    my_database = client.Betfair_IT
    Collection = my_database.Vincente
    Collection.remove()


    for a, b, c, d, e  in zip(Partita, StartingIn, V1, X, V2):
        Index = Partita.index(a)
        BetfairIT_vincente = { 
        "N°": Index, 
        "Data" : b,
        "Partita": a,
        '1' : c,
        'X' : d,
        '2' : e,
        'Update' : now(),
        }
        Collection.insert(BetfairIT_vincente);