import re

# Basic Patterns
# a, X, 9, < - ordinary characters just match themselves exactly
# The meta-characters which do not match themselves because
# they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
# . (a period) - matches any single character except newline '\n'
# a|A - 'a' or 'A'
# [\s\S] - matches any single character (including '\n')
# \w - matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]
# \W - matches any non-word character
# \b - boundary between word and non-word
# \B - non-boundary between word and non-word
# \s - matches a single whitespace character [ \n\r\t\f]
# \S - matches any non-whitespace character
# \t, \n, \r - tab, newline, return
# \d - decimal digit [0-9]
# ^ = start, $ = end - match the start or end of the string; \A, \Z
# \ - inhibit the "specialness" of a character
# \NNN - znak w formacie ósemkowy
# \xNN - znak w formacie szesnastkowy
# So, for example, use \. to match a period or \\ to match a slash

# Search
# matchObject = re.search(pattern, input_str, flags=0)
match = re.search(r'iii', 'piiig')  # match.group() == "iii"
match = re.search(r'igs', 'piiig')  # match == None
match = re.search(r'..g', 'piiig')  # match.group() == "iig"
match = re.search(r'\d\d\d', 'p123g')  # match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!')  # match.group() == "abc"

# Repetition
# + - 1 or more occurrences of the pattern to its left
# * - 0 or more occurrences of the pattern to its left
# ? - match 0 or 1 occurrences of the pattern to its left
# {2} - 2 occurrences
# {2, 5} - from 2 to 5 occurrences
# {3, } - at least 2 occurrences
# {, 7} - at most 7 occurrences
match = re.search(r'pi+', 'piiig')  # match.group() == "piii"
match = re.search(r'i+', 'piigiiii')  # match.group() == "ii"
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')  # match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')  # match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')  # match.group() == "123"
match = re.search(r'^b\w+', 'foobar')  # match == None
match = re.search(r'b\w+', 'foobar')  # match.group() == "bar"

# Square Brackets
# [abc] matches 'a' or 'b' or 'c'
# [.] matches '.' (not any single character)
# [^>] matches all character which are not '>' ('^' inverts the square bracket)

# Find email alice-b@google.com
re.search(r'[\w.-]+@[\w.-]+', 'purple alice-b@google.com monkey').group()
# Find tags
str = '<b>foo</b> and <i>so on</i>'
re.findall(r'<[^>]*>', str)  # ['<b>', '</b>', '<i>', '</i>']

# Group Extraction
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())   # 'alice-b@google.com' (the whole match)
    print(match.group(1))  # 'alice-b' (the username, group 1)
    print(match.group(2))  # 'google.com' (the host, group 2)

# Find all the matches and return
# matchList = re.findall(pattern, input_str, flags=0)
# matchList = re.finditer(pattern, input_str, flags=0)
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w.-]+@[\w.-]+', str)
print(emails)  # ['alice@google.com', 'bob@abc.com']

# Find patterns in file
re.findall(r'pattern', open('text.txt').read())

# findall and Groups
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  # [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print(tuple[0])  # username
    print(tuple[1])  # host

# Non-Capturing Group ?:
# When parenthesis ( ) groupings in the pattern, but you don't want to extract
str = '1st, 2nd, 3rd, 4th, 29.03.2017'
match = re.findall(r'([0-9]+)(?:st|nd|rd|th)', str)  # [1, 2, 3, 4]

# Greedy vs. Non-Greedy
# '+' and '*' are greedy (goes as far as is it can)
# '+?' and '*?' are non-greedy (top as soon as it can)
str = '<b>foo</b> and <i>so on</i>'
re.search(r'<.*>', str).group()  # '<b>foo</b> and <i>so on</i>'
re.search(r'<.*?>', str).group()  # '<b>'

# Replacement
# re.sub(pattern, replacement_pattern, input_str, count, flags=0)
