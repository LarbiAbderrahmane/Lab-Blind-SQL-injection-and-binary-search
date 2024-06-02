# Lab-Blind-SQL-injection-and-binary-search
Another approach to solve portswigger lab: Blind SQL injection, using Binary Search.

## **Binary search Solution**

using binary search to narrow down the number of requests needed to find the password.\
Check this Medium Write-Up for more details : 

## **Installation**
This script is tested in Python 3.11.8

To install it, follow these steps:

1. Clone the repository: 
**`git clone git@github.com:LarbiAbderrahmane/Lab-Blind-SQL-injection-and-binary-search.git`**\
or \
**`git clone https://github.com/LarbiAbderrahmane/Lab-Blind-SQL-injection-and-binary-search.git`**\
2. Navigate to the project directory: \
**`cd Lab-Blind-SQL-injection-and-binary-search`**\
3. Install httpx: \
**`pip install httpx`**

## **Usage**

To use the code, follow these steps:

1. Open the project in your favorite code editor.
2. Copy the raw headers intercepted from Burpsuite inside raw_http_headers (without the request line e.g. GET / ...).
3. Execute **`raw_headers_to_dict.py`** and copy the output in the return value of **inject_headers** function in **`funcs.py`**
4. Change **URL** variable content to your lab's url.  
5. Now you're ready to execute **`main.py`**

## **Contributing**

Performance can be improved using async programming or multiprocessing to send the http requests in efficient way, if you think you are able to achieve that, or any other changes you see better fit, then be my guest.

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes.
4. Test your changes.
5. Commit your changes.
6. Push your changes to your forked repository.
7. Submit a pull request.
