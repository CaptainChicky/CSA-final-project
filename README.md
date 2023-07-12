# Comp Sci A Final Project
This is the final project for our AP CSA class.

# Structure
## Main
 - *RSA_main* folder contains all the RSA python code. Within main is all the functions, and the keygen, decrypt, and encrypt contain the driver programs.
 - *server.py* contains the flask server file, *static* folder is the styling and js for the *templates* folder html files of the chat room. Both devices must be connected via LAN (same network that has a group policy that doesn't block LAN connections aka iPhone hotspots or home wifi, and not school wifi) to be able to see packets sent by the eventlet flask server. Access the server via the hosting device's IP address on port 8081. Of course, you can port forward to access the chatroom from somewhere other than LAN, but whatever.

## Other
 - *java-tmp* folder is just files when we experimented with RSA in java.

## Dependencies
For js, you need socket.io, which is linked in the *chat.html* file, and a local copy is also provided.  
For python, you need flask, flask_login, and eventlet.

## Note for closure
External fonts have been imported into */static/fonts/*. The *socket.io* js file is still used via a link, but a local copy is provided in */static/*. The CSS for the chatroom is written very noobishly so the messages may not display right. This will not be fixed, by us, at least. You're welcome to try.
