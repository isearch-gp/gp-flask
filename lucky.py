# lucky.py

#import json
import requests, sys, webbrowser
from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify
from flask import request

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

# use SerpAPI format for easy digest
data = {
    "search_metadata": {},
    "search_parameters": {},
    "search_information": {},
    "ads": [],
    "local_map": {},
    "local_results": [],
    "related_questions": [],
    "answer_box": {},
    "organic_results": [],
    "related_searches": [],
    "pagination": {}
    }

@app.route("/", methods=['GET'])
def hello():
   return "Hello World"

@app.route("/raw", methods=['GET'])
def raw():
    q = request.args.get('q') # not requests
    
# from
# https://automatetheboringstuff.com/chapter11/
    #res = requests.get('http://google.com/search?q=' + q)
    res = requests.get('https://google.com/search?q=' +q+ "&oq="+q+"&hl=en&gl=us&sourceid=chrome&ie=UTF-8")
    res.raise_for_status()
    return (res.text) # show html page
    
@app.route("/search", methods=['GET'])
def search():
# from
# https://automatetheboringstuff.com/chapter11/
    print('Googling...') # display text while downloading the Google page
    q = request.args.get('q') # not requests
    print("q = "+q)

    #res = requests.get('http://google.com/search?q=' + q)
    res = requests.get('https://google.com/search?q=' +q+ "&oq="+q+"&hl=en&gl=us&sourceid=chrome&ie=UTF-8")
    res.raise_for_status()

#   print some html reponse information
    print("status = "+str(res.status_code))
    if "blocked" in res.text:
        print( "we've been blocked")
    print (res.headers.get("content-type", "unknown"))

# Retrieve top search result links.
    soup = BeautifulSoup(res.text,"html.parser")
#    print("soup ="+soup)
#    print(soup)

# Open a browser tab for each result.
    linkElems = soup.select('.r a') # osearch links and titles
    abstractElems = soup.select('.st') # osearch snippets
    relatedSearches = soup.select('.aw5cc a')
#    relatedQuestions = soup.select('.st span')
    for resultStats in soup.find_all("div", "sd"):
        result_count = resultStats.contents
#        print("s")

#    for titleElems in soup.find_all("div", "r"):
    titleElems = soup.select('.r a')
    for x in range(len(titleElems)):
#        print(".")
        title = titleElems[x].text
#        print("title = "+titleElems[x].text+"\n")
        print("title = "+title+"\n")
        link = titleElems[x]["href"]
#        print("link = "+titleElems[x]["href"]+"\n")
        print("link = "+link+"\n")

    print("\n\nlinkElems")
    print(*linkElems, sep = "\n")

    print("\n\nabstractElems")
    print(*abstractElems, sep = "\n")

    print("\n\nrelatedSearches")
    print(*relatedSearches, sep = "\n")

#    print(*resultStats, sep = "\n")
#    total_results = int(resultStats[0])
    total_results = result_count

    print("\n\ntotal_results")
    print (total_results)

#    print(*titles, sep = "\n")

#    print(*links, sep = "\n")

#    return "Searching for "+q
#    return (res.text) # show html page
#    return (soup) # show BAD
    html="<!DOCTYPE doctype html>"
#    for x in range(len(resultStats)):
#        html=html+"<p>"+str(resultStats[x])+"<br>"
    for x in range(len(total_results)):
         html=html+"<p>"+total_results[x]+"<br>"
    html=html+"<h2>Related Searches</h2>"
    for x in range(len(relatedSearches)):
        html=html+str(relatedSearches[x])+"<br><br>"
    html=html+"<h2>Related Questions</h2>"
    html=html+"<h2>Organic Results</h2>"
    for x in range(len(linkElems)): 
        html=html+str(linkElems[x])+"<br>"
        html=html+str(abstractElems[x])+"<br><br>"

    # then gen JSON

    json1 = '{ "search_parameters": { "q": "'+q
    json2 = '"}, "search_information": { "total_results": '+total_results[0]
    json3 = '},"related_questions": [],"organic_results": ['
#
#    position?
#    title
#    link
#    snippet
#    date - optional
#
    json4 = '],  "related_searches": [ '
#
#    query
#    link
#
    json5 = ']}'

    return (html) # show URLs 

@app.route("/json", methods=['GET'])
def json():
# from
# https://automatetheboringstuff.com/chapter11/
    q = request.args.get('q') # not requests
    print("q = "+q)
    print('Googling...') # display text while downloading the Google page
    #res = requests.get('http://google.com/search?q=' + q)
    res = requests.get('https://google.com/search?q=' +q+ "&oq="+q+"&hl=en&gl=us&sourceid=chrome&ie=UTF-8")
    res.raise_for_status()

#   print some html reponse information
    print("status = "+str(res.status_code))
    if "blocked" in res.text:
        print( "we've been blocked")
    print (res.headers.get("content-type", "unknown"))

# Retrieve top search result links.
    soup = BeautifulSoup(res.text,"html.parser")
#    print("soup ="+soup)
#    print(soup)

# Open a browser tab for each result.
    linkElems = soup.select('.r a') # osearch links and titles
    abstractElems = soup.select('.st') # osearch snippets
    relatedSearches = soup.select('.aw5cc a')
#    relatedQuestions = soup.select('.st span')
    for resultStats in soup.find_all("div", "sd"):
        result_count = resultStats.contents
#        print("s")

#    for titleElems in soup.find_all("div", "r"):
    titleElems = soup.select('.r a')
    for x in range(len(titleElems)):
        title = titleElems[x].text
        print("title = "+title+"\n")
        link = titleElems[x]["href"]
        print("link = "+link+"\n")

    print("\n\nlinkElems")
    print(*linkElems, sep = "\n")

    print("\n\nabstractElems")
    print(*abstractElems, sep = "\n")

    print("\n\nrelatedSearches")
    print(*relatedSearches, sep = "\n")

#    print(*resultStats, sep = "\n")
#    total_results = int(resultStats[0])
    total_results = result_count

    print("\n\ntotal_results")
    print (total_results)

    # then gen JSON
    data1 = data # empty struct
    data1["search_parameters"]["q"]= q
    data1["search_information"]["total_results"]= total_results[0]
    # "organic_results": []
    for x in range(len(titleElems)):
        position = x
        title = titleElems[x].text
        #print("title = "+title+"\n")
        link = titleElems[x]["href"][7:] # remove /url?q=
        #print("link = "+link+"\n")
        snippet = abstractElems[x].text
        data1["organic_results"].append({ "position": position, "title" : title, "link": link, "snippet": snippet })

    # "related_questions": []

    # "related_searches": [ ]
    for x in range(len(relatedSearches)):
        query = relatedSearches[x].text
        link = relatedSearches[x]["href"]
        data1["related_searches"].append({ "query": query, "link": link })

    return(jsonify(data1))

if __name__ == "__main__":
	app.run()

