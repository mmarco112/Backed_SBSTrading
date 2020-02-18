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
import re
from utils import *




def Pinnacle_ENG():
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-extensions")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-notifications");

    driver = webdriver.Chrome(executable_path= r"C:\Users\marco\Desktop\chromedriver.exe", options=options)



    driver.get('https://www.pinnacle.com/en/soccer/italy-serie-a/matchups')
    time.sleep(15)
    html = driver.page_source
    soup = BeautifulSoup(html)

    Text = []
    SquadraCasa = []
    SqadraTrasferta = []
    V1 = []
    Draw = []
    V2 = []

    for x in soup.find_all('div', {'class': 'style_vertical__2mKTx'}):
        
        for partita in x.find_all('div', {'data-test-id': 'Event.Row'}):
            for gameInfo in partita.find_all('a', {'data-test-id': 'Event.GameInfo'}):
                for firstDiv in gameInfo.select('div:nth-child(1)'):
                    SquadraCasa.append(firstDiv.text)
                for secondDiv in gameInfo.select('div:nth-child(2)'):
                    SqadraTrasferta.append(secondDiv.text)
            for v1 in partita.find_all('a', {'data-test-designation': 'home'}):
                V1.append(v1.text)
            for draw in partita.find_all('a', {'data-test-designation': 'draw'}):
                Draw.append(draw.text)
            for v2 in partita.find_all('a', {'data-test-designation': 'away'}):
                V2.append(v2.text)

    # print(SquadraCasa)
    # print(SqadraTrasferta)
    Partita=[]

    for a, b  in zip(SquadraCasa, SqadraTrasferta):
        squadracasa = a 
        squadratrasferta = b
        partita = squadracasa + ' - ' + squadratrasferta
        Partita.append(partita)

    Partita[:] = [x for x in Partita if "Home" not in x]


    client = MongoClient("mongodb://marco:Arkaton11!@cluster0-shard-00-00-7vwyj.mongodb.net:27017,cluster0-shard-00-01-7vwyj.mongodb.net:27017,cluster0-shard-00-02-7vwyj.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

    my_database = client.Pinnacle
    Collection = my_database.Vincente
    Collection.remove()

    for a, b, c, d  in zip(Partita, V1, Draw, V2):
        Pinnacle_vincente = { 
        "Partita": a,
        '1' : b,
        'X' : c,
        '2' : d,
        'Update' : now(),
        }
        Collection.insert(Pinnacle_vincente);