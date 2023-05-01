# UDP-Client-Server
## TestRadio.tx
C code for "anchor" sensors, which should be placed in the center of every room in a building.  
Runs on a timer, pinging phones' locations every second

## Server
Python code to be left running on a server. Receives information from the anchors over UDP, uses it to perform a GET request from our DB, then makes a POST to save the updated information to the DB.

## Client
Sample program to send UDP packets that would be received by the server. Was used during python code testing.

# Usage
## Run TestRadio.tx
Must be loaded onto KolidaES sensors using kes-term.

## Run Python Server
```
python3 server.py
```

## Compile & run c client code
```
gcc client.c -o client
```
```
./client
```
