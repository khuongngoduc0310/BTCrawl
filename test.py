import requests
from bs4 import BeautifulSoup
import re
import json
url = "https://www.missuniverse.com/paula-mehmetukaj"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
country_filter = re.compile('[^a-zA-Z]')
for i in soup.find_all('span',attrs={'style' : 'letter-spacing:0.03em'}):
            if (re.compile("Age.*").match(i.text)):
                age = i.text[-2:]
                break
print("https://www.instagram.com/" + soup.find('span',attrs={'style' : 'font-weight:bold'},text="Instagram ").parent.text[11:] + "/")