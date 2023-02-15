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
print(tweet_df['sentiment'].value_counts())
my_file = open("negative-words.txt", "r")
data = my_file.read() 
negative_list = data.split("\n")
my_file.close()
print(len(negative_list))
my_file = open("positive-words.txt", "r")
data = my_file.read()
positive_list = data.split("\n")
my_file.close()
print(len(positive_list))
def count_words(comment, words): 
    count = 0
    for word in comment.split(' '):
        if word in words:
            count += 1
    return count

tweet_df['number_positive_words'] = tweet_df["tweet"].apply(count_words, words=positive_list)
tweet_df['number_negative_words'] = tweet_df["tweet"].apply(count_words, words=negative_list)
tweet_df['semi_normalised_scores'] = round(tweet_df['number_positive_words'] / (tweet_df['number_negative_words']+1), 2)
#tweet_df.to_csv('senti_score_search_football.csv')
polarity = [round(sent.polarity_scores(i)['compound'], 2) for i in tweet_df['tweet']]
tweet_df['Vader_score'] = polarity
tweet_df.drop('Tweet_id', inplace=True, axis=1)
#print(tweet_df.head(100))
# tweet_df.to_csv('scores_football.csv')
tweet_df["sentiment"].value_counts().plot(kind='bar')
plt.xlabel("Sentiment", labelpad=14)
plt.ylabel("Number of Tweets", labelpad=14)

tweet_df.plot(
   x='semi_normalised_scores', 
   y='Vader_score', 
   kind='scatter', 
   c='red',
)
plt.show()


