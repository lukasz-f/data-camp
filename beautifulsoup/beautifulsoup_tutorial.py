from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'html.parser')  # Python’s html.parser
BeautifulSoup(html_doc, "lxml")  # lxml’s HTML parser
BeautifulSoup(html_doc, "lxml-xml")  # lxml’s XML parser
BeautifulSoup(html_doc, "xml")  # lxml’s XML parser
BeautifulSoup(html_doc, "html5lib")  # html5lib
BeautifulSoup(html_doc, "xml")  #

BeautifulSoup(open("index.html"))  # open file and parse with best available parser

print(soup.prettify())
print(soup.get_text())

# Find first
soup.title  # <title>The Dormouse's story</title>
soup.title.name  # title
soup.title.string  # The Dormouse's story
soup.title.parent.name  # head
soup.p  # <p class="title"><b>The Dormouse's story</b></p>
soup.p['class']  # ['title']
soup.a  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
soup.a.text  # Elsie
soup.a['href']  # http://example.com/elsie
soup.find('a')  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
soup.find(text='Lacie')  # 'Lacie'
soup.find(id="link3")  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
soup.find(class_="sister")  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# Find all
soup('a')
soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

for link in soup.find_all('a'):
    link.get('href')
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

soup(text='Lacie')  # ['Lacie']
soup(id='link2')  # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
soup(class_='sister')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.a.next_element  # 'Elsie'
soup.a.next_sibling  # ',\n'
soup.a.find_next_sibling('a')  # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
