import requests
import re

link = input()
text = requests.get(link).text
links = re.findall(r'https:.+?html', text)
