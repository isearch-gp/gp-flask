# gp-flask

## Google Proxy Flask API using Python, Response and BeautifulSoup

![GitHub tag](https://img.shields.io/github/tag/mkobar/gp-flask.svg)
![Code Style](https://img.shields.io/badge/code_sytle-none-red.svg)
![Linted](https://img.shields.io/badge/linted-none-red.svg)
[![Known Vulnerabilities](https://snyk.io/test/github/mkobar/gp-flask/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/mkobar/gp-flask?targetFile=requirements.txt)
![Security Scanner](https://img.shields.io/badge/security_scanner-none-red.svg)
![Website](https://img.shields.io/website-up-down-green-red/https/gp-python.herokuapp.com%2Fsearch%3Fhl%3Den%26gl%3Dus%26ie%3DUTF-8%26q%3Dcats%2Bvideo.svg)

I originally tried to "port" Googler to an API but found it much easier to do the web scraping myself.  Still need to add a lot of functionality (see ToDo below).

This proxy also displays web and raw web output (for debug)

## Usage:
```
lucky.py - Python Web Scaping API in Flask

        Options:
        -h   --help       this message
        -v N --verbose=N  verbose output

                 0 = Info
                 3 = JSON payload counts
                 5 = JSON payload elements
                 6 = raw JSON payload
```

## Python Dev setup
### activate Virtual ENV (venv)/workon hello

C:\Users\x\Documents\GitHub\gp-flask>.\venv\Scripts\activate

C:\Users\x\Documents\GitHub\gp-flask>workon hello

### deactivate

(venv) C:\Users\x\Documents\GitHub\gp-flask>deactivate

### run the Flask app

(venv) C:\Users\x\Documents\GitHub\gp-flask>python lucky.py

## Endpoints to test

Show response as web page (Raw HTML - what Google returns)
http://localhost:5000/raw?q=malpractice

Show response as web page (from parsed response data)
http://localhost:5000/search?q=malpractice

Send response as JSON (for API)
http://localhost:5000/json?q=malpractice

This can also be done interactivaly with Python on the command line:
```
(hello) C:\Users\x\Documents\GitHub\gp-flask>python

>>> import requests
>>> response = requests.get("http://127.0.0.1:5000/json?q=malpractice")
>>> response.json()
```
or with cURL:
```
curl http:///127.0.0.1:5000/json?q=malpractice
```

## Advanced Topics (ToDo)

- CI Testing
- API Testing
- Handling Network Errors

### Scraper stuff
- Sessions and Cookies
- Delays and Backing Off
- Spoofing and Cycling the User Agent
- Using Proxy Servers
- Setting Timeouts
- Use Selenium web driver
- Use PhantomJS for headless JS support

### Service stuff
- Authentication
- Logging

## Links

http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

https://blog.hartleybrody.com/web-scraping-cheat-sheet/

More here: [Iterative Search](http://iterativesearch.com)

