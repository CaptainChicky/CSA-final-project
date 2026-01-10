# Comp Sci A Final Project
This is the final project for our AP CSA class.<br>
This isn't the most organized project, as the RSA stuff and the chatroom server stuff are basically completely disjoint, but it's whatever since it worked well enough for the class project presentation lol (we basically exchanged the RSA encryption stuff on the chatroom over LAN).

If the person I worked with ever sees/revisits this repo again, just know that you were a good friend :) 

# Structure
## Main
 - `/RSA_main/` folder contains all the RSA python code. Within main is all the functions, and the keygen, decrypt, and encrypt contain the driver programs which you actually run to generate keys, or encrypt/decrypt.
 - `server.py` contains the flask server file you run to start the LAN server, `/static/` folder is the styling and js for the `/templates/` folder html files of the chat room. Both devices must be connected via LAN (same network that has a group policy that doesn't block LAN connections aka iPhone hotspots or home wifi, and not school wifi) to be able to see packets sent by the eventlet flask server. Access the server via the hosting device's IP address on port 8081. Of course, you can port forward to access the chatroom from somewhere other than LAN, but thats more trouble than it's worth so whatever.

## Other
 - `/java-tmp/` folder is just files when we experimented with RSA in java. It's a mess compared to the complete `/RSA_main/` python scripts but still useful code to archive.
   - `Decrypt.java` is a substitution cipher decrypter (not RSA).
   - `keygen.java` is an abstract base class for RSA keys.
   - `PrivateKey.java` and `PublicKey.java` generate RSA private and public key respectively.
   - `Main.java` just demonstrates key generation.

## Dependencies
For js, you need socket.io, which is linked in the `/templates/chat.html` file, and a local copy is also provided.  
For python, you need flask, flask_login, and eventlet. 

*Eventlet only works with python version v3.11 and below right now, but you can check the website or whatever to see if it updated or not.*

## Note for closure
External fonts have been imported into `/static/fonts/`. The *socket.io* js file used in `/templates/chat.html` is still used via a link, but a local copy is provided in `/static/`. The CSS for the chatroom is written very noobishly so the messages may not display right. This will not be fixed, by us, at least. You're welcome to try.
