""" hello.py """

import json
#import googler
import requests 
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

@app.route("/search/<string:q>", methods=['GET'])
def search(q):
    print("q = "+q)
    """search = googler(q)
    results_object = [r.jsonizable_object() for r in search.results]
    print(json.dumps(results_object, indent=2, sort_keys=True, ensure_ascii=False))"""
#    return "Searching for "+q
# from
# https://stackoverflow.com/questions/22623798/google-search-with-python-requests-library
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=headers_Get)

    soup = BeautifulSoup(r.text, "html.parser")
    output = []
    for searchWrapper in soup.find_all('h3', {'class':'r'}): #this line may change in future based on google's web page structure
        url = searchWrapper.find('a')["href"] 
        text = searchWrapper.find('a').text.strip()
        result = {'text': text, 'url': url}
        output.append(result)

    return output
    

if __name__ == "__main__":
	app.run()

