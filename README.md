# gp-flask
Google Proxy Flask API using Python, Response and BeautifulSoup

I originally tried to "port" Googler to an API but found it much easier to do the web scraping myself.  Still need to add a lot of functionality (see ToDo below).

This proxy also displays web and raw web output (for debug) 

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

## Advanced Topics (todo)

- Sessions and Cookies
- Delays and Backing Off
- Spoofing and Cycling the User Agent
- Using Proxy Servers
- Setting Timeouts
- Handling Network Errors
- Use Selenium web driver
- Use PhantomJS for headless JS support

## Links

http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/

https://blog.hartleybrody.com/web-scraping-cheat-sheet/

