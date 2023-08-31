from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('')
bs= BeautifulSoup(html,'html.parser')