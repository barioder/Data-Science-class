import requests
from html.parser import HTMLParser

url = "https://en.wikipedia.org/wiki/Data_science"

text = requests.get(url).content.decode('utf-8')

print(text[:1000])

print("-----------------------------------------------------------------------------------")

# Creating a custom parser
class MyHtmlParser(HTMLParser):

    script = True
    res = ""
    # check if it is an opening tag
    def handle_starttag(self, tag, attrs):
        if tag.lower() in ["script", "style"]:
            self.script = True

    # check if it is a closing tag
    def handle_endtag(self, tag):
        if tag.lower() in ["script", "style"]:
            
            self.script = False
    
    # Handling data between tags
    def handle_data(self, data):
        # returns nothing(None) without processing the data
        if str.strip(data) == "" or self.script:
            return
        
        self.res += " " + data.replace('[edit]', "")


# An instance of the parser
parser = MyHtmlParser()

parser.feed(text)  #using the feed method to pass the data to the parser 

text = parser.res

print(text[:1000])