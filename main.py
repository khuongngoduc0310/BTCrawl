import requests
from bs4 import BeautifulSoup
import re
import json

def save_json(data, file):
    with open(file,'w',encoding='utf-8') as f:
        json.dump(data,f,indent=4,ensure_ascii=False)

response = requests.get("https://www.missuniverse.com/delegates");
soup = BeautifulSoup(response.text, 'html.parser')
linkElements = soup.find_all('a',attrs= {'data-testid' : "linkElement", 'target' : "_self"},class_="_2k7xj");
links = []
for x in linkElements:
    links.append(x['href'])
names = []
country_filter = re.compile('[^a-zA-Z]')
for link in links:
    res = requests.get(link)
    soup = BeautifulSoup(res.text, 'html.parser')
    try:
        name = " ".join(link[29:].split("-")).title()
        country = country_filter.sub("",soup.find('span',text=re.compile("Country.*")).parent.text[8:])
        #age = soup.find('span',attrs={'style' : 'font-weight:bold'},text=re.compile('Age.*')).text[-2:]
        age = ""
        for i in soup.find_all('span',attrs={'style' : 'letter-spacing:0.03em'}):
            if (re.compile("Age.*").match(i.text)):
                age = i.text[-2:]
                break
        ins = "https://www.instagram.com/" + soup.find('span',attrs={'style' : 'font-weight:bold'},text=re.compile("Instagram.*")).parent.text[11:] + "/";
        data = {
            'name': name,
            'country' : country,
            'age' : age,
            'ins' : ins
        }
        names.append(data)
    except Exception as e:
        print('Exeption : ', e)
        print(link)
save_json(names,'data.json')
