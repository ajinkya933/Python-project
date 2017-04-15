from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time,datetime,json
import sentiment_mod as s #imported the file created by using pickles

#These are 4 values got from twitter by creating an application in twitter
ckey = '53Oi8ofbfLqhANzJMYSd5O57O'
csecret = 'g8ZaVJ6ZU67uoMZjVvCjILfSLwzDvmlcX8vSAQGynCEI1bJAKk'
atoken = '142544162-StI793M4NP8SrZSfMrM2hoiWhzPh5h9YSoXGwhoO'
asecret = 'sUY3YRLBTWh877tuFjeDfTrbOcfbTDkbE0ZcAPBJKJZ66'

class listener(StreamListener):

    def on_data(self, data):
        try:
            all_data = json.loads(data)     #Use json to apply on tweet.
            tweet = all_data["text"]
            sentiment_value,confidence = s.sentiment(tweet)
            print(tweet,sentiment_value,confidence)
            if confidence*100 >= 80:    #So more than 0.8 confidence value counted as accurate result for sentniment
                output = open("Barbershop.txt","a")  #Save tweets with sentiment and confidence value
                output.write(tweet)
                output.write("      ")
                output.write(sentiment_value)
                output.write(":::::")
                output.write(confidence)
                output.write("\n")
                output.close()
            return True
        except BaseException as e:
            print (e)
            time.sleep(5)
    def on_errror(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Barbershop"],languages=['en'])     #Write the word that you want to search in tweeter and also language filter applied
