import requests
from html.parser import HTMLParser
import sys
import nlp_rake
import matplotlib.pyplot as plt

from wordcloud import WordCloud


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

# creating an insance of the nlp_rake libray 
# we set the max number of words in the keyword phrase,
# min frequency the key phrase is listed 
# min number of characters in the key phrase 
extractor = nlp_rake.Rake(max_words=2, min_freq=3, min_chars=5)
result = extractor.apply(text)  # applies the keyword extraction 

print("--------------Insight from the text data--------------  ")
print(result) #returns a list ordered by keyphrases in terms of importance 

# Visualizing the results 
# A function that takes in list of key value pairs and generates a graph 
def plot(pair_list):
    k,v = zip(*pair_list)

    # plot the bars and y axis values 
    plt.bar(range(len(k)), v)
    # x axis tick lables 
    plt.xticks(range(len(k)),k, rotation ="vertical")
    plt.show()


plot(result)

# Using a work cloud to visualuze the data
wordCloud = WordCloud(background_color='white', width=800, height=600)# the dimensions are for the cloud canvas
# size for the figure 
plt.figure(figsize=(15,7))
plt.imshow(wordCloud.generate_from_frequencies({k:v for k,v in result }))
plt.show()