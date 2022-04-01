# Networks
PDU - protocol data unit.
## OSI Layers
## Application
**PDU: Data**

High-level APIs, including resource sharing, remote file access.
### HTTP
### HTTPS
### REST 
### RESTful
### RPC
### RIP
### FTP
### SMTP
### POP
### IMAP
### BGP
### DHCP
### DNS
### SSH


## Presentation
**PDU: Data**

Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption.

### Char encoding
### Data compression
### Encryption/decryption

### MIME
### SSL/TLS

TLS

## Session
**PDU: Data**
Managing communication sessions, i.e., continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes.

The session layer controls the dialogues (connections) between computers. It establishes, manages and terminates the connections between the local and remote application.

In the modern TCP/IP system, the session layer is non-existent and is simply part of TCP.

The session layer is commonly implemented explicitly in application environments that use remote procedure calls.



### Sessions

## Transport
PDU: Segment (TCP), Datagram (UDP)

Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing.

### TCP
### UDP
### SCTP

## Network
**PDU: Packet**

Structuring and managing a multi-node network, including addressing, routing and traffic control.

The network layer provides the functional and procedural means of transferring packets from one node to another connected in "different networks". A network is a medium to which many nodes can be connected, on which every node has an address and which permits nodes connected to it to transfer messages to other nodes connected to it by merely providing the content of a message and the address of the destination node and letting the network find the way to deliver the message to the destination node, possibly routing it through intermediate nodes.

Message delivery at the network layer is not necessarily guaranteed to be reliable; a network layer protocol may provide reliable message delivery, but it need not do so.

### IP
### IPsec
### ICMP
### ARP

## Data link
**PDU: frame**

Reliable transmission of data frames between two nodes connected by a physical layer

The data link layer provides node-to-node data transfer—a link between two directly connected nodes. It detects and possibly corrects errors that may occur in the physical layer. It defines the protocol to establish and terminate a connection between two physically connected devices. It also defines the protocol for flow control between them.

### MAC (Medium Access Control)
responsible for controlling how devices in a network gain access to a medium and permission to transmit data.
### LLC (Local Link Control)
responsible for identifying and encapsulating network layer protocols, and controls error checking and frame synchronization.

### PPP
The Point-to-Point Protocol (PPP) is a data link layer protocol that can operate over several different physical layers, such as synchronous and asynchronous serial lines.

## Physical 
**PDU: bit, symbol**
Transmission and reception of raw bit streams over a physical medium.

The physical layer is responsible for the transmission and reception of unstructured raw data between a device and a physical transmission medium. It converts the digital bits into electrical, radio, or optical signals. Layer specifications define characteristics such as voltage levels, the timing of voltage changes, physical data rates, maximum transmission distances, modulation scheme, channel access method and physical connectors. This includes the layout of pins, voltages, line impedance, cable specifications, signal timing and frequency for wireless devices. Bit rate control is done at the physical layer and may define transmission mode as simplex, half duplex, and full duplex.