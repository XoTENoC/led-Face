## Server side

1. Start by creating a REST api that store all the bit map information
2. when new infomation is added to the server push an update out to the clients
3. Convert any new information from pictures into bit maps

## Client side

1. Reciving the update request from the server
2. Pulling the new information from the server
3. Checking back every few seconds for update on the information, in the case of missing an updated request from the server.