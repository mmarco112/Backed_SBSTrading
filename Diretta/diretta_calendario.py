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


def Diretta_calendario():
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--disable-application-cache")
    options.add_argument("--disable-extensions")
    options.add_argument("--log-level=3")
    options.add_argument("--disable-notifications");

    driver = webdriver.Chrome(executable_path= r"C:\Users\marco\Desktop\chromedriver.exe", options=options)

    driver.get('https://www.diretta.it/serie-a/calendario/')
    time.sleep(5)
    title = driver.title
    html = driver.page_source
    soup = BeautifulSoup(html)
    
    SquadraCasa = []
    SquadraTrasferta = []
    DataPartita = []

    # myEleme= soup.find('div', {'class': 'event__more event__more--static'})

    myEleme = driver.find_element_by_class_name('event__more')
    
    while myEleme.is_displayed():
        driver.execute_script("arguments[0].click();", myEleme)
        print('I')
        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html)
        for x in soup.find_all('div', {'class': 'sportName soccer'}):
            for squadracasa in x.find_all('div', {'class': 'event__participant event__participant--home'}):
                SquadraCasa.append(squadracasa.text)
            for squadratrasferta in x.find_all('div', {'class': 'event__participant event__participant--away'}):
                SquadraTrasferta.append(squadratrasferta.text)
            for datapartita in x.find_all('div', {'class': 'event__time'}):
                DataPartita.append(datapartita.text)

        break

            
      
    client = MongoClient("mongodb://marco:Arkaton11!@cluster0-shard-00-00-7vwyj.mongodb.net:27017,cluster0-shard-00-01-7vwyj.mongodb.net:27017,cluster0-shard-00-02-7vwyj.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

    my_database = client.Diretta
    Collection = my_database.Calendario_SerieA
    Collection.remove()

    for a, b, c  in zip(SquadraCasa, SquadraTrasferta, DataPartita):
        Diretta_calendario = { 
        "Partita": a + ' - ' + b,
        'DataPartita' : c,
        'Update' : now(),
       }
        Collection.insert(Diretta_calendario);          

  

    # print(SquadraCasa)
    
    # print(SquadraTrasferta)
    # print(len(SquadraCasa))
    # print(len(SquadraTrasferta))



