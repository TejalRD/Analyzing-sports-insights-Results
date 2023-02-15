import pandas as pd
import html
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from nltk.stem.porter  import PorterStemmer
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import nltk
# nltk.download('vader_lexicon')
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sent = SentimentIntensityAnalyzer()

tweet_df = pd.read_csv ('C:/Users\Chelsea\Downloads/Twitter_Plots/twitter_football.csv')
tweet = tweet_df.Tweet_id
tweetList = []
res = []
list_of_tweets = tweet_df['Tweet_id'].to_list()
ch = ':'
for x in list_of_tweets:
    listOfWords = x.split(ch, 1)
    
    if len(listOfWords) > 0: 
        tweets = listOfWords[1]
        pattern = re.compile('\W')
        res.append(re.sub(pattern, ' ', tweets))

tweet_df['tweet'] = res

def get_sentiment(tweets):
    blob = TextBlob(tweets)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'
tweet_df['sentiment'] = tweet_df['tweet'].apply(get_sentiment)
tweet_df["sentiment"].value_counts().plot(kind='bar')
plt.show()
