# Program z zajęć
# python 2
import urllib2
response = urllib2.urlopen('http://www.gutenberg.org/cache/epub/50133/pg50133.txt')
html = response.read()

# python 3
import urllib.request
url = 'http://www.gutenberg.org/cache/epub/50133/pg50133.txt'
response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
