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
from Betfair.betfair_vincente_Eng import *
from Betfair.betfair_vincente_IT import *
from Pinnacle.pinnacle_ENG import *
from Diretta.diretta import *
from Diretta.diretta_calendario import *

betfair_vincente_ENG()
betfair_vincente_IT()
Pinnacle_ENG()
Diretta_stat()
Diretta_calendario()


