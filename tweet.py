from __future__ import absolute_import, print_function
from flask import Flask

import urllib
import tweepy

app = Flask(__name__)


consumer_key="Vm2Y4C9RsZFWQMBLUqcGvtpoK"
consumer_secret="Xa9Ux7jZf11ZUzvCd4etsS9cwRJNiC5GqDLnHYUiF4X9K7VLNI"
access_token="1937164880-bsMHtfTyja6eMOZutW9T7LbVjijRBvYezHAJieO"
access_token_secret="ejqfTpMCO3ceigKhyrY4twhGXnpi7xU7ChSyszUGtTQJo"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        tweets.append(status.text)
        print(len(tweets))
        if(len(tweets) >= 10):
        	print(len(tweets))
        	return False;

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['trump'])

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

@app.route('/')
def hello_world():
    return str(tweets)


@app.route('/deeznuts')
def deez():
	return 'gotteem'

if __name__ == '__main__':
    app.run()