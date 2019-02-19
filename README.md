# HttpPy

Python based HttpPy for more comfortable requests.

### Installation
#### PiPY
```sh
(env)$ pip install HttpPy
```

### Usage
#### Single Request
Sometimes you may just want to send a single request. To achieve that there are some flags ready to use.
```sh
(env)$ python -m HttpPy -t post -u http://127.0.0.1:8000 -d '{"user": "eve", "password": "12345"}'
```
 - **-t / --type**  
Represents the request verb [ get | post | put | patch | options | delete ] to use.
 - **-u / --url**  
Is the endpoint to reach.
 - **-d / --data**  
 Represents the body of the request.


#### Several Requests
If you need to send several requests, you can use a file as an input.
```sh
(env)$ python -m HttpPy -i example.request
```
 - **-i / --input**  
 Is the path to a file that contains the requests especifications.

*An example of a post request inside example.request file may be:*  
```
## This comment is important to parse correctly the request
POST http://127.0.0.1:8000
Headers
ContentType: application/json
Authorization: Basic QWxhZGRpbjpvcGuIHN1c2FtZQ==
{
  "data": "data one",
  "data 2": "data two"
}
```  

#### Extra flags
There are two optional flags that may help you:
- **-v / --verbose**  
The presence of this flag will indicate that the especifications of requests and a more detailed reponse will be printed in the screen.
- **-p / --parallel**  
This flag is intented to help with performance and excecution times. Internally indicates that several threads are going to be used for the requests.
