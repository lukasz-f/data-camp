import string
import codecs

words = {}
with codecs.open('pg50133.txt', 'r', 'utf8') as file:
    for each_line in file:
        for each_word in each_line.split():
            word = each_word.strip(string.punctuation).lower()
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

top10_words = sorted(words, key=words.get, reverse=True)[:10]
top10_dict = {value: words[value] for value in top10_words}
print('All words:', words)
print('Top 10 words:', top10_words)
print('Top 10 dictionary:', top10_dict)
