# If you need to get API data from a database or need to send an API request to a server, this automation script is a convenient tool for you. Using the Urllib3 module, you can get and post API requests.

# pip install urllib3
import urllib3

# Fetch API data
url = "https://api.github.com/users/psf/repos"
http = urllib3.PoolManager()
response = http.request('GET', url)
print(response.status)
print(response.data)

# Post API data
url = "https://httpbin.org/post"
http = urllib3.PoolManager()
response = http.request('POST', url, fields={'hello': 'world'})
print(response.status)