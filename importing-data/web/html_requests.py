# Import package
import requests


# Performing HTTP requests in Python using requests #
# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# Packages the request, send the request and catch the response
r = requests.get(url)

# Extract the response
text = r.text

# Print the html
print(text)