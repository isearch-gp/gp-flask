# lucky.py

import json
import requests, sys, webbrowser
from bs4 import BeautifulSoup
from flask import Flask
app = Flask(__name__)

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }


@app.route("/", methods=['GET'])
def hello():
   return "Hello World"

@app.route("/raw/<string:q>", methods=['GET'])
def raw(q):
# from
# https://automatetheboringstuff.com/chapter11/
    res = requests.get('http://google.com/search?q=' + q)
    res.raise_for_status()
    return (res.text) # show html page
    
@app.route("/search/<string:q>", methods=['GET'])
def search(q):
    print("q = "+q)
# from
# https://automatetheboringstuff.com/chapter11/
    print('Googling...') # display text while downloading the Google page
    res = requests.get('http://google.com/search?q=' + q)
    res.raise_for_status()

# Retrieve top search result links.
    soup = BeautifulSoup(res.text,"html.parser")
#    print("soup ="+soup)
#    print(soup)

# Open a browser tab for each result.
    linkElems = soup.select('.r a')
#    abstractElems = soup.select('.st span')
    abstractElems = soup.select('.st')
    relatedSearches = soup.select('.aw5cc a')

    print(*linkElems, sep = "\n")

    print(*abstractElems, sep = "\n")

    print(*relatedSearches, sep = "\n")

#    return "Searching for "+q
#    return (res.text) # show html page
#    return (soup) # show BAD
    html="<!DOCTYPE doctype html>"
    html=html+"<h2>Related Searches</h2>"
    for x in range(len(relatedSearches)):
        html=html+str(relatedSearches[x])+"<br><br>"
    html=html+"<h2>Related Questions</h2>"
    html=html+"<h2>Organic Results</h2>"
    for x in range(len(linkElems)): 
        html=html+str(linkElems[x])+"<br>"
        html=html+str(abstractElems[x])+"<br><br>"
    return (html) # show URLs 

if __name__ == "__main__":
	app.run()

