import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

# Accessing the sample book
with open("miracle_in_the_andes.txt", "r") as file:
    book = file.read()

# Applying Regex to collect most used words
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1
d_list = [(value,key) for (key, value) in d.items()]
sorted(d_list, reverse=True)

# Applying NLP to avoid stop words
english_stopwords = stopwords.words("english")

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))

# Applying Sentiment Analysis to find the most positive and negative chapter

analyzer = SentimentIntensityAnalyzer()
book_scores = analyzer.polarity_scores(book)

pattern = re.compile("Chapter [0-9]+")
chapters = re.split(pattern, book)

for number, chapters in enumerate(chapters):
    scores = analyzer.polarity_scores(chapters)
    print(f"Chapter {number} has {scores}")
