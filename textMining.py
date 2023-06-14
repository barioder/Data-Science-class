import requests
from html.parser import HTMLParser

url = "https://en.wikipedia.org/wiki/Data_science"

text = requests.get(url).content.decode('utf-8')

print(text[:1000])



