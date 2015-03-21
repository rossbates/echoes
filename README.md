echoes
======
Echoes is a Python library for working the (unofficial) [Amazon Echo](http://www.amazon.com/oc/echo/) API. 
The Echo is a really nice piece of hardware but I found it's capabilities limited. Hopefully 
people can use this code to make their Echo do some fun and interesting things like text your friends, order
pizza, or turn off the lights.

Example
-------
The project includes a file (example.py) which shows hows to initialize a connection to the API and 
make a set of basic requests.
    
    
Notes
-----
* Amazon does not provide an official API. Things could break at anytime.
* When making a request for /cards or /tasks the limit command doesn't return consistent results. Use 1 for the most recent, or 50 for all.
* Script needs write access to the directory where it's running to store a cookie.

Setup
-----
You will need to create a file called 'config.json' in your project directory to store your Echo login credentials.

```javascript
    { 
        "email": "caesar@alexandria.org", 
        "password": "who.me?" 
    }
```

Dependencies
------------
* Requests
* BeautifulSoup 4
