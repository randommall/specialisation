import requests
import logging
import http.client


# since the request module does not have a direct equivalent of -v option
# in curl, we can achieve a similar functionality by enabling debug logging.
# logging.basicConfig(level=logging.DEBUG)

http.client.HTTPConnection.debuglevel = 1

url = 'http://localhost:5000/api/v1/unauthorized/'

response = requests.get(url)

print(response.text)
