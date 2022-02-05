# SSRF

 This room aims at providing the basic introduction to Server Side request forgery vulnerability(SSRF).
 
 ## Task 1 What is SSRF? 
 
 SSRF is a vulnerability in web applications whereby an attacker can make further HTTP requests through the server. An attacker can make use of this vulnerability to communicate with any internal services on the server's network which are generally protected by firewalls.





![illustartion](https://i.imgur.com/cAozwRZ.png)


Now if you focus on the above diagram, In a normal case the attacker would only be able to visit the website and see the website data. The server running the website is allowed to communicate to the internal GitLab or Postgres database, but the user may not, because the firewall in the middle only allows access to ports 80 (HTTP) and 443 (HTTPS).However, SSRF would give an attacker the power to make a connection to Postgres and see its data by first connecting to the website server, and then using that to connect to the database. Postgres would think that the website is requesting something from the database, but in reality, it's the attacker making use of an SSRF vulnerability in website to get the data. The process would usually be something like this: an attacker finds an SSRF vulnerability on a website. The firewall allows all requests to the website. The attacker then exploits the SSRF vulnerability by forcing the webserver to request data from the database, which it then returns to the attacker. Because the request is coming from the webserver, rather than directly from the attacker, the firewall allows this to pass.


#### Deploy the VM 

` ans: no answer needed `





  <br>  <br>  <br>


# Task 2 Cause of the Vulnerability

The main cause of the vulnerability is (as it often is) blindly trusting input from a user. In the case of an SSRF vulnerability, a user would be asked to input a URL (or maybe an IP address). The web application would use that to make a request. SSRF comes about when the input hasn't been properly checked or filtered.

Let's look at some vulnerable code:

Example 1: PHP

Assume there is an application that takes the URL for an image, which the web page then displays for you. The vulnerable SSRF code would look like this:




``` php
<?php

if (isset($_GET['url']))

{
  $url = $_GET['url'];
  $image = fopen($url, 'rb');
  header("Content-Type: image/png");
  fpassthru($image);

}  
  ```
  
  
This is simple PHP code which checks if there is information sent in a 'url' parameter then, without performing any kind of check on it, the code simply makes a request to the user-submitted URL. Attackers essentially have full control of the URL and can make arbitrary GET requests to any website on the Internet through the server -- as well as accessing resources on the server itself.


Example 2: Python 


``` python 

from flask import Flask, request,  render_template, redirect
import requests


app = Flask(__name__)


@app.route("/")
def start():
    url = request.args.get("id")
    r = requests.head(url, timeout=2.000)
    return render_template("index.html", result = r.content)

if __name__ == "__main__":
      app.run(host = '0.0.0.0')
      
```
      
      
      
    
      
      
      
      

The above example shows a very small flask application which does the same thing:

1) It takes the value of the "url" parameter.

2) Then it makes a request to the given URL and shows the content of that URL to the user.

Again we see that there is no sanitisation or any kind of check performed on the user input. This is why you should always try as many different payloads as you can when testing an application


#### Read the above.

` ans: no answer needed `
