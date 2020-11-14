from bs4 import BeautifulSoup
import requests
import re
import sys

patern = r"name=\"a\d+\" type=\"\w+\" value=..."
if len (sys.argv) > 1:
       url = sys.argv[1]
else:
       url = input('Owned by Duxk: ')  # Честно спиздил из гугла


source_code = requests.get(url)
html = BeautifulSoup(source_code.text, 'html.parser')
question = html.find_all('div', {"class": "label"})
question = str(question).split('</div>, <div class=\"label\">')

for i in range(len(question)):
    tasks = str(html).split('<div class=\"q\" id="')
    temp = tasks[i + 1]
    TempAnswer = re.findall(patern, temp)
    if len(TempAnswer) > 1:
        LastTemp = ((str(TempAnswer).split('name="')[1].split('"')[0])[1:])
        print('Задание ' + LastTemp)
        for answer in TempAnswer:
            print(answer[-2].replace('1', '+').replace('0', '-'))
