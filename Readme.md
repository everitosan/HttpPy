# HttpClient

Python based HttpClient for more comfortable requests.

### Usage  
#### Process a file  
If you need to send several requests consecutively, you can use a file as an input.
 - --i/--input = Route to open the file
```
(env)$ python --i "example.request"
```
#### Process with arguments  
Sometimes you may just want to send a single request. To achieve that there are some flags ready to use.
 - --t/--type = The request verb to use
 - --u/--url = The endpoint to reach
 - --d/--data = The data to send
 ```
(env)$ python --t [get|post|put|patch|delete] --u http://127.0.0.1:8000 --d '{"user": "eve", "password": "12345"}'
```
