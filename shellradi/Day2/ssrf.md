# SSRF

 This room aims at providing the basic introduction to Server Side request forgery vulnerability(SSRF).
 
 ## Task 1 What is SSRF? 
 
 SSRF is a vulnerability in web applications whereby an attacker can make further HTTP requests through the server. An attacker can make use of this vulnerability to communicate with any internal services on the server's network which are generally protected by firewalls.





![illustartion](https://i.imgur.com/cAozwRZ.png)


Now if you focus on the above diagram, In a normal case the attacker would only be able to visit the website and see the website data. The server running the website is allowed to communicate to the internal GitLab or Postgres database, but the user may not, because the firewall in the middle only allows access to ports 80 (HTTP) and 443 (HTTPS).However, SSRF would give an attacker the power to make a connection to Postgres and see its data by first connecting to the website server, and then using that to connect to the database. Postgres would think that the website is requesting something from the database, but in reality, it's the attacker making use of an SSRF vulnerability in website to get the data. The process would usually be something like this: an attacker finds an SSRF vulnerability on a website. The firewall allows all requests to the website. The attacker then exploits the SSRF vulnerability by forcing the webserver to request data from the database, which it then returns to the attacker. Because the request is coming from the webserver, rather than directly from the attacker, the firewall allows this to pass.


#### Deploy the VM 

` ans: no answer needed `

