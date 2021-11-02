# Plan: 
___
- Client: class
    - able to send to central server 
    - able to encrypt 
    - able to authenticate
    
- Server: class
    - able to decrypt
    - connect to database 
    - route messages - Multiple simultaniously = multiplex and demultiplex
    - should work by creating a new therad
- 
    
### plan 

login:
    creat a login page 
create account page:
    do that 
generate public key stuff 

in database: username, public key, password 

make it so that we have to enter the username of the person you want to message -> see if this is doable 

encorperate rsa with client not with server 

create a nice interface for sending messages 

set up mongo-server to store username, public key, password  and make it so that 
everyone has a login for atlas 
    