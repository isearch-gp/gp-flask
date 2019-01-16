# gp-flask
Google Proxy Flask API using Python, Response and BeautifulSoup

This proxy also displays web and raw web output (for debug) 

## activate Virtual ENV (venv)/workon hello

C:\Users\x\Documents\GitHub\gp-flask>.\venv\Scripts\activate

C:\Users\x\Documents\GitHub\gp-flask>workon hello

## deactivate

(venv) C:\Users\x\Documents\GitHub\gp-flask>deactivate

## run the Flask app

(venv) C:\Users\x\Documents\GitHub\gp-flask>python lucky.py

## endpoints to test

Show response as web page (Raw HTML)
http://localhost:5000/raw?q=___malpractice___

Show response as web page (from parsed response data)
http://localhost:5000/search?q=___malpractice___

Send response as JSON (for API)
http://localhost:5000/json?q=___malpractice___

This can also be done interactivaly with Python on the command line:
```
(hello) C:\Users\x\Documents\GitHub\gp-flask>python

>>> import requests
>>> response = requests.get("http://127.0.0.1:5000/json?q=malpractice")
>>> response.json()
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

