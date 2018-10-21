import nltk
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk import word_tokenize
nltk.download("stopwords")
nltk.download("punkt")

import string
import csv
import re
import itertools

ARTICLES_CSV = "articlesFinal.csv"
SCOPE = 10 # most common words. e.g. 10 most common words

def extract_key(v):
    return v[0]

### open csv file from webscraper
articles = []
with open(ARTICLES_CSV) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        articles.append(row[4])

### process the article ###

combined_articles_freq = []

for article in articles:

        article = re.sub(r'[^\w]', ' ', article) # remove special punctuation (hyphens) 
        article = article.lower() # make text lowercase
        article = article.replace("'s", "") # remove 's (possessive)

        # punctuation removal
        punc_remove = str.maketrans("", "", string.punctuation) # setup to remove punctuation
        article = article.translate(punc_remove) # remove punctuation

        # remove stopwords
        stop_words = stopwords.words('english') # set stopwords language
        word_tokens = nltk.word_tokenize(article) # tokenize words
        more_stop_words = ['said', 'says', 'say' '5etfw', 'xa0jr', 'article', 'href', 'refsrc', 'xa0', 'twsrc', 'kpmg', 'cbc', 'https', 'com']
        common_words = ['oh', 'hi', 'hello', 'bye', 'ok', 'said', 'says', 'say', 'told', 'who', 'name', 'would', 'could', 'should', 'he', 'she', 'how', 'come', 'like', 'per', 'canada']
        stop_words.extend(more_stop_words)
        stop_words.extend(common_words)

        # clean article
        cleaned_article = []
        for word in word_tokens:
                if word not in stop_words:
                        cleaned_article.append(word)

        # get word frequencies and get list of most common words
        freqs = nltk.FreqDist(cleaned_article)
        pop_freqs = freqs.most_common(SCOPE)

        # convert pop_freqs into list (was a originally a list of tuples)
        l_pop_freqs = []
        for i in range(len(pop_freqs)):
                l_pop_freqs.append(list(pop_freqs[i]))

        combined_articles_freq.extend(l_pop_freqs)

# combine all frequencies
combined_articles_freq = sorted(combined_articles_freq, key=extract_key)

# code below from https://stackoverflow.com/questions/773/how-do-i-use-pythons-itertools-groupby
aggregate = [[k,[x[1] for x in g]] for k, g in itertools.groupby(combined_articles_freq, extract_key)]

# sum frequencies
for i in range(len(aggregate)):
        aggregate[i][1] = sum(aggregate[i][1])

# get factor to normalize word frequencies
total = 0
for i in range(len(aggregate)):
        total += aggregate[i][1]

# normalize word frequencies vector
for i in range(len(aggregate)):
        aggregate[i][1] = round(aggregate[i][1]/total, 3)

myCSV = open('frequencies.csv', 'w')
with myCSV:
        writer = csv.writer(myCSV)
        writer.writerows(aggregate)