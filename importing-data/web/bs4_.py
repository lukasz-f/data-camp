# Import packages
import requests
from bs4 import BeautifulSoup

# Parsing HTML #
# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response
r = requests.get(url)

# Extracts the response as html
html_doc = r.text

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)


# getting the text #
# Get the title of Guido's webpage
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)


# getting the hyperlinks #
# Find all 'a' tags (which define hyperlinks)
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
