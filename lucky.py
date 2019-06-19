# lucky.py

#import json
import requests, sys, getopt, webbrowser
from bs4 import BeautifulSoup
from flask import Flask
from flask import jsonify
from flask import request
import copy

app = Flask(__name__)

# internal switches/from args (default values)
verbose = 0
help = 0
output = ''

# read commandline arguments, first
fullCmdArguments = sys.argv

# - further arguments
argumentList = fullCmdArguments[1:]

#print(argumentList)
unixOptions = "ho:v:"  
gnuOptions = ["help", "output=", "verbose="]  

# validate args sent
try:  
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:  
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

# evaluate given options
for currentArgument, currentValue in arguments:  
    if currentArgument in ("-v", "--verbose"):
        #print ("enabling verbose mode of (%s)", currentValue)
        print ("verbose mode of "+str(currentValue))
        verbose = int(currentValue)
    elif currentArgument in ("-h", "--help"):
        #print ("displaying help")
        print (sys.argv[0]+" - Python Web Scaping API in Flask\n")
        print ("\tOptions:")
        print ("\t-h   --help       this message")
        print ("\t-v N --verbose=N  verbose output\n")
        print ("\t\t 0 = Info (default)")
        print ("\t\t 3 = JSON payload counts")
        print ("\t\t 5 = JSON payload elements")
        print ("\t\t 6 = raw JSON payload")
        sys.exit(1)
    elif currentArgument in ("-o", "--output"):
        print ("enabling special output mode (%s)", currentValue)
        output = currentValue

# headers to use in Get
headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/62.0',
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
    res = requests.get('https://www.google.com/search?q=' +q+
                       "&oq="+q+"&hl=en&gl=us&sourceid=chrome&ie=UTF-8",
                       headers=headers_Get
                      )
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
    #res = requests.get('https://google.com/search?q=' +q+ "&oq="+q+"&hl=en&gl=us&sourceid=chrome&ie=UTF-8")
    res = requests.get('https://www.google.com/search?q=' +q+
                       "&oq="+q+"&hl=en&gl=us&sourceid=chrome&ie=UTF-8",
                       headers=headers_Get
                      )
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
#    for resultStats in soup.find_all("div", "sd"):
#        result_count = resultStats.contents
#        print("s")
    print(".resultStats")
    for i in soup.select("#resultStats"):
       print("i.text: ")
       print(i.text)
       j = i.text.split()
       print ("["+j[0]+"]")
       print (j[1])
       if (j[0] == "About"):
           #if ( j[1].isnumeric() ):  has commas
           if ( j[1][0].isdigit() ):
               result_count = j[1]
               if ( j[2] == "Million") or (j[2] == "million") :
                   result_count += ",000,000"
               elif ( j[2] == "Thousand") or (j[2] == "thousand"):
                   result_count += ",000"
               elif ( j[2] == "Results") or (j[2] == "results"):
                   result_count += ""
               else: 
                   result_count = '-1'
                   assert "Google sent a new resultStats string"
           else:
               result_count = '-2'
       else:
           result_count = '-3'
       print("resultStats =", result_count)

       #for m, k in enumerate(j):
       #    print ("k = ", k)
       #    print (j[m])
    print("resultStats2 =", result_count)


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

    if (verbose > 3):
       try:
          print("\n\nlinkElems")
          print(*linkElems, sep = "\n")

          print("\n\nabstractElems")
          print(*abstractElems, sep = "\n")

          print("\n\nrelatedSearches")
          print(*relatedSearches, sep = "\n")
        except IndexError as e:
            # just skip it for now
            print( e)
            #print sys.exc_type

#    print(*resultStats, sep = "\n")
#    total_results = int(resultStats[0])
    total_results = result_count

    if (verbose > 3):
       print("\n\ntotal_results")
       print (total_results)

#    print(*titles, sep = "\n")

#    print(*links, sep = "\n")

#    return "Searching for "+q
#    return (res.text) # show html page
#    return (soup) # show BAD
    html="<!DOCTYPE doctype html><head></head><body>"
#    for x in range(len(resultStats)):
#        html=html+"<p>"+str(resultStats[x])+"<br>"
#   for x in range(len(total_results)):
#        html=html+"<p>"+total_results[x]+"<br>"
#        if (verbose > 5):
#            print ("<p>"+total_results[x]+"<br>")
    html=html+"<p>"+total_results+"<br>"
    if (verbose > 5):
        print ("<p>"+total_results+"<br>")
    html=html+"<h2>Related Searches</h2>"
    for x in range(len(relatedSearches)):
        html=html+str(relatedSearches[x])+"<br><br>"
        if (verbose > 5):
            print(str(relatedSearches[x])+"<br><br>")
    html=html+"<h2>Related Questions</h2>"

    html=html+"<h2>Organic Results</h2>"
    for x in range(len(linkElems)): 
        html=html+str(linkElems[x])+"<br>"
        if (verbose > 5):
            print("linkElems="+str(len(linkElems))+" x="+str(x)+"\n")
        # can have link without snippet?
        if (verbose > 5):
            print("linkElems="+str(len(linkElems))+" abstractElems="+str(len(abstractElems))+" x="+str(x)+"\n")

        #if ((len(abstractElems)) >= x-1):
        #if (abstractElems[x]):
        try :
            html=html+str(abstractElems[x])+"<br><br>"
        except IndexError as e:
            # just skip it for now
            print( e)
            #print sys.exc_type

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
    res = requests.get('https://google.com/search?q=' +q+
                       "&oq="+q+"&hl=en&gl=us&sourceid=chrome&ie=UTF-8",
                      headers=headers_Get)
    res.raise_for_status()

#   print some html reponse information
    if (verbose > 0):
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
#    for resultStats in soup.find_all("div", "sd"):
#        result_count = resultStats.contents
#        print("s")
    print(".resultStats")
    for i in soup.select("#resultStats"):
       print("i.text: ")
       print(i.text)
       j = i.text.split()
       print ("["+j[0]+"]")
       print (j[1])
       if (j[0] == "About"):
           #if ( j[1].isnumeric() ):  has commas
           if ( j[1][0].isdigit() ):
               result_count = j[1]
               if ( j[2] == "Million") or (j[2] == "million") :
                   result_count += ",000,000"
               elif ( j[2] == "Thousand") or (j[2] == "thousand"):
                   result_count += ",000"
               elif ( j[2] == "Results") or (j[2] == "results"):
                   result_count += ""
               else: 
                   result_count = '-1'
                   assert "Google sent a new resultStats string"
           else:
               result_count = '-2'
       else:
           result_count = '-3'
       print("resultStats =", result_count)

       #for m, k in enumerate(j):
       #    print ("k = ", k)
       #    print (j[m])
    print("resultStats2 =", result_count)


#    for titleElems in soup.find_all("div", "r"):
    titleElems = soup.select('.r a')
    for x in range(len(titleElems)):
        title = titleElems[x].text
        print("title = "+title+"\n")
        link = titleElems[x]["href"]
        print("link = "+link+"\n")

    if (verbose > 3):
        print("\n\nlinkElems")
        print(*linkElems, sep = "\n")

        print("\n\nabstractElems")
        print(*abstractElems, sep = "\n")

    if (relatedSearches):
        if (verbose > 3):
          print("\n\nrelatedSearches")
          print(*relatedSearches, sep = "\n")

#    print(*resultStats, sep = "\n")
#    total_results = int(resultStats[0])
    total_results = result_count

    if (verbose > 3):
        print("\n\ntotal_results")
        print (total_results)

    # then gen JSON
    #data1 = data # empty struct
    #data1 = data[:] # empty struct
    # https://stackoverflow.com/questions/5105517/deep-copy-of-a-dict-in-python
    data1 = copy.deepcopy(data) # empty struct
    if (verbose > 6):
        print("post-copy, pre-fill data1: ")
        print(data1)

    data1["search_parameters"]["q"]= q
    data1["search_information"]["total_results"]= total_results[0]
    # "organic_results": []
    for x in range(len(titleElems)):
        position = x
        title = titleElems[x].text
        #print("title = "+title+"\n")
        link = titleElems[x]["href"][7:] # remove /url?q=
        #print("link = "+link+"\n")
	# can have link without snippet?
        if (verbose > 5):
            print("linkElems="+str(len(linkElems))+" abstractElems="+str(len(abstractElems))+" x="+str(x)+"\n")
        if (len(abstractElems) > x):
           snippet = abstractElems[x].text
        else:
           snippet = ''
        data1["organic_results"].append({ "position": position, "title" : title, "link": link, "snippet": snippet })

    # "related_questions": []

    # "related_searches": [ ]
    if (relatedSearches):
        for x in range(len(relatedSearches)):
            query = relatedSearches[x].text
            link = relatedSearches[x]["href"]
            data1["related_searches"].append({ "query": query, "link": link })

    if (verbose > 6):
        print("returned data1 out:")
        print(data1)
    return(jsonify(data1))

if __name__ == "__main__":
	app.run()

