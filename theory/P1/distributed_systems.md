# Large scale system design

1. Performance optimization
2. App stability
3. CAP Theorem

## Scaling
With horizontal-scaling it is often easier to scale dynamically by adding more machines into the existing pool; Vertical-scaling is usually limited to the capacity of a single server and scaling beyond that capacity often involves downtime and comes with an upper limit.

### Horizontal scaling
Adding more servers.

Cassandra and MongoDB as they both provide an easy way to scale horizontally by adding more machines to meet growing needs.
### Vertical scaling
Adding more resources to existing servers.

MySQL as it allows for an easy way to scale vertically by switching from smaller to bigger machines. However, this process often involves downtime.

relation db -> noSQL db

### Sharding
### NoSQL DB

## Load balancing
Typically a load balancer sits between the client and the server accepting incoming network and application traffic and distributing the traffic across multiple backend servers using various algorithms.

### Where
1. Between the user and the web server
2. Between web servers and an internal platform layer, like application servers or cache servers
3. Between internal platform layer and database.

### Benefits
1. Users experience faster, uninterrupted service. 
2. Service providers experience less downtime and higher throughput.
3. Smart load balancers provide benefits like predictive analytics that determine traffic bottlenecks before they happen.


### Cons
1. The load balancer can be a single point of failure
**Solution:**
A second load balancer can be connected to the first to form a cluster.
Each LB monitors the health of the other and, since both of them are equally capable of serving traffic and failure detection.


### How
**Health Checks**
Load balancers should only forward traffic to “healthy” backend servers. To monitor the health of a backend server, “health checks” regularly attempt to connect to backend servers to ensure that servers are listening. If a server fails a health check, it is automatically removed from the pool, and traffic will not be forwarded to it until it responds to the health checks again.
### Strategies
1. **Least Connection method** -  directs traffic to the server with the fewest active connections.
Useful when there are a large number of persistent client connections which are unevenly distributed between the servers.
2. **Least response time** - directs traffic to the server with the fewest active connections and the lowest average response time.
3. **Least bandwidth method** - selects the server that is currently serving the least amount of traffic measured in megabits per second (Mbps).
4. **Round Robin** - cycles through a list of servers and sends each new request to the next server.
Useful when the servers are of equal specification and there are not many persistent connections.
5. **Weigthed Round Robin** - Each server is assigned a weight (an integer value that indicates the processing capacity). Servers with higher weights receive new connections before those with less weights and servers with higher weights get more connections than those with less weights.
Handle servers with different processing capacities.
5. **IP Hash** - a hash of the IP address of the client is calculated to redirect the request to a server.
### Client side 

#### Pros: 
1. No more single point of failure as in the case of the traditional load balancer approach.
2. Less network latency as the client can directly invoke the backend servers removing an extra hop for the load balancer.
3. Reduced cost as the need for server-side load balancer goes away.

#### Cons:
1. Initially setting is more difficult than server side LB
2. Clients must be trusted.



How to find server adddress and detect peer failure.
-> Client queries service registry,
-> Service sends heartbeat to registry, to prvent its record from expiring.


### Server side
#### Pros:
1. Easy set up - simple client configuration.
2. Clients may be untrusted: all traffic goes through LB, where it can be checked.
3. Clients are not aware of the backend servers.

#### Cons:
1. LB is a single point of failure
2. Extra cost - need to buy LB server (or more).
3. Extra latency because client connects to server through LB.

How to avoid single point of failure -> Mirror Pair. Add another Load balancer.

## Fail-safe (Reliability)
Consistency/Eliminating single point of failure.

## Reliability
### Netflix monkey chaos

## Replication
for a stateful service.

## Master Election
### Raft
### Paxos


## Performance
Caching + Load Balancing
### Geographical Load balancing
### Data repicas synchronisation

## Caching 
### Algorithms
1. Cache aside
2. Write trough
3. Read through

### Cache invalidation

### Memcached
### Redis

## Logging
### RabbitMQ
### Amazon SQS/SNS
### Kafka

## System Monitor
### System health criterions
How to measure

## Deployment
### Mesos
### Distributed Systems deployment problems




