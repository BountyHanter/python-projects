import bs4
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd

url = 'https://market.dota2.net/?r=Arcana&search=Feast%20of%20Abscession&sd=desc'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
block = soup.find_all('div', class_ = "price")
numbers=[d.text.replace(u'\xa0', u'') for d in block]
print(numbers)