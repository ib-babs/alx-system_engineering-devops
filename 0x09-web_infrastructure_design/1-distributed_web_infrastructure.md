![alt](https://imgur.com/uRBEXAG)
## Q: For every additional element, why you are adding it
- 2 servers added to reduce the SPOF and downtime in case of updating and maintenance of any of the server
- Load balancer - For balancing and sharing the loads among these servers

## Q: What distribution algorithm your load balancer is configured with and how it works
- Round Robin Algorithm
- This algorithm shares the load among the server as they follow.

## Q: Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
- Load-balancer implemented here is Active-Active setup
- Active-Active setup is a setup where all the available servers are in action i.e they are working
- Active-Passive setup is a setup where one server is in action and the other servers are not in action. The passive servers are to be in action if any failure in the active server 

## Q:How a database Primary-Replica (Master-Slave) cluster works
- Primary-Replica (Master-Slave) cluster is a situation where the Primary(Master) is the main database server and its operations include read-write. Master resources is shared with the Replica(Slave) cluster. Replica cluster replicates data from Master server and its operations are read-only, distributing the read workload and improving overall performance. 

## Q: What is the difference between the Primary node and the Replica node in regard to the application
- Primary Node/server typically responsible for handling both read and write operation. It serves as the authoritative source for data changes
- Replica node/server replicates Primary Node. Its operations are read-only, distributing the read workload and improving overall performance. 


# Issues with this infrastructure:

## Q: Where are SPOF
SPOF in this infrastructure lies among the servers.

## Q: Security issues (no firewall, no HTTPS)
The connection in this infrastructure is insecure as the protocol is HTTP and also there is no firewalls that serve as preventive measure for any breaches between the private network and the outer network

## Q: No monitoring
No alert if something is unusual or that could make the computer not work properly happens.