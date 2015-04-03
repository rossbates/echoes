echoes
======
Echoes is a Python library for working the (unofficial) [Amazon Echo](http://www.amazon.com/oc/echo/) API. 
The Echo is a nice piece of hardware but it's capabilities are currently somewhat limited. Hopefully 
people can use this code to make their Echo do some fun and interesting things.

Example
-------
The project includes a file (example.py) which shows hows to initialize a connection to the API and 
make a set of basic requests.
    
    
Notes
-----
* Amazon does not provide an official API for the Echo. Things could break at anytime.
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

When starting, echoes will check for an existing cookie then try to make an basic 
request to check that it's still valid. If either scenario fails the API will log 
you in and store the cookie.

Amazon uses bot detection, so there is potential a captcha will be served on login.
If this happens echoes will throw an error, unfortunately there's no way around this
right now. I've found this only happens when you login repeatedly from the same IP
in a short period of time. To be safe I'd recommend using a throw away account for your
Echo if you are going to use this.

Dependencies
------------
* Requests
* BeautifulSoup 4
