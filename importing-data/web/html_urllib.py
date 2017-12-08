# Import packages
from urllib.request import urlopen, Request


# Printing HTTP request results in Python using urllib #
# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request
request = Request(url)

# Sends the request and catches the response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Extract the response
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()
