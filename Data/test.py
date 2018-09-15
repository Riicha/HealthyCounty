import xlrd
from glob2 import glob
import json
import pymongo
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
import string
import re


# test = "Aleutians West [4]".translate({ord(k): None for k in digits}).replace('[]','')
test = re.compile('[a-zA-Z ]{6,}',re.I).findall('Aleutians')[0].rstrip()

print(len(test))