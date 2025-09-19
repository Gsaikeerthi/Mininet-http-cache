This folder cosists of two folders named basic and star along with the report for the assignment 1.

Basic folder contains of two python files named client.py and sever.py.
It contains a file named h1.pcap which consists of the pcap traces captured at H1.

To run the program run the following commands in terminal

cd /home/p4/tutorials/exercises/basic
make
xterm h1
xterm h2

in h1's terminal run
bash h1-arp.sh
python client.py (here, enter the IP address as “10.0.1.2”)

in h2's terminal run
bash h2-arp.sh
python server.py (here, enter the IP address as “10.0.1.2”)


The client code runs an infinte while loop to take the requests.
User is prompted to provide the request as GET or PUT or DELETE.
If user wants to exit from the process they have to type EXIT.
Every input given by user should be enclosed in " " i.e double quotes

To exit the server user has to enter Crt + C.

The response from the server will be visible on the h1 terminal.


Star folder contains three python files named client.py, cache.py and sever.py.
It contains a folder named pcap_observation which consists of the pcap traces captured at H1, H2, H3.

To run the program run the following commands in terminal:

cd /home/p4/tutorials/exercises/star
make
xterm h1
xterm h2
xterm h3

in h1's terminal run
bash h1-arp.sh
python client.py (here, enter the IP address as “10.0.1.2”)

in h2's terminal run
bash h2-arp.sh
python cache.py (here, enter the IP address as “10.0.1.2”)

in h3's terminal run
bash h3-arp.sh
python server.py (here, enter the IP address as “10.0.1.3”)


The client code runs an infinte while loop to take the requests.
User is prompted to provide the request as GET or PUT or DELETE.
If user wants to exit from the process they have to type EXIT.
Every input given by user should be enclosed in " " i.e double quotes

To exit the cache/server user has to enter Crt + C.

The response from the cache will be visible on the h1 terminal.