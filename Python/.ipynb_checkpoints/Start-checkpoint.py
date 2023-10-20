
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# initialize the sentiment analyzer
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# get user input
text = input("Hey this pizza is very yum")

# analyze sentiment of the text
sentiment = sia.polarity_scores(text)

# print the sentiment analysis results
print(f"Sentiment Analysis Results: {sentiment}")
