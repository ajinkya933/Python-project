from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


#consumer key, consumer secret, access token, access secret.
ckey="dV0faJUajP8x4NMbxabTmjPRX"
csecret="jG07LKfQ7CaboiFAjbEZzyzZdPDCDsQRhN4PKxL5bZcwVu62pG"
atoken="1220591857-PsSxsoiC9TU060kNYToGJ3PEGzwHbXzzx6parOp"
asecret="ojWPzdpuqY2bFd3CN9eCc3BbSl3siME8rLNxWnXPGTtwL"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        
        print((tweet))
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
