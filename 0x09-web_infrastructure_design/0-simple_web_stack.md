![alt](https://imgur.com/wwPaQNA)

## Q: What is a server
- Server is any physical/virtual machine that other machines rely upon for distribution of resources

## Q: What is the role of the domain name
- Domain name is translated by the resolver server mapping it by to the IP address in order to access the website the domain name holds.

## Q: What type of DNS record www is in www.foobar.com
- CNAME Record

## Q: What is the role of the web server
- Web server is responsible for providing the clients with the HTTP static-content response

## Q: What is the role of the application server
- Its role is more of web server however, its content is dynamic and communication between the client and the server is not always HTTP request-response.

## Q: What is the role of the database
- Database stores persistent data

## Q: What is the server using to communicate with the computer of the user requesting the website
- Web Server

# Issues with this infrastructure
1. Single Point of Failure(SPOF) - Any arising problem on this server causes user inability to access the resources from server as a result of only one server

2. Downtime when maintenance needed (like deploying new code web server needs to be restarted) - As said earlier, any maintenance to the server disable user from accessing the server as server needs to be down for some moment

3. Cannot scale if too much incoming traffic - Meaning, no load balancing between the client and the server.