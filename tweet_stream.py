# -*- coding: utf-8 -*-

from threading import Thread
from queue import Queue

from twython import Twython
from twython import TwythonStreamer
from requests.exceptions import ChunkedEncodingError

# Input your credentials below
consumer_key = 'xxx'
consumer_secret = 'xxx'
token = 'xxx'
token_secret = 'xxx'
twitter = Twython(consumer_key, consumer_secret, token, token_secret)
tweet_queue = Queue()

class TwitterStream(TwythonStreamer):

    def __init__(self, consumer_key, consumer_secret, token, token_secret, tqueue):
        self.tweet_queue = tqueue
        super(TwitterStream, self).__init__(consumer_key, consumer_secret, token, token_secret)

    def on_success(self, data):
        if 'text' in data:
            self.tweet_queue.put(data)

    def on_error(self, status_code, data):
        print(status_code)
        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()


def stream_tweets(tweets_queue):
    try:
        stream = TwitterStream(consumer_key, consumer_secret, token, token_secret, tweets_queue)
        # You can filter on keywords, or simply draw from the sample stream
        stream.statuses.filter(track='your,search,phrases,hashtags,etc',  language='en')
        # stream.statuses.sample(language='en')
    except ChunkedEncodingError:
        # Sometimes the API sends back one byte less than expected which results in an exception in the
        # current version of the requests library
        stream_tweets(tweet_queue)


def process_tweets(tweets_queue):
    while True:
        tweet = tweets_queue.get()
        # Do something with the tweet! You can use the global "twitter" variable here.
        # Next line prints output encoded in ASCII so it displays in Windows 10 command terminal
        print(tweet['text'].encode('ascii','ignore'))
        # Next line prints only the tweet author's info and not the whole tweet
        # print(tweet['user']['id'], tweet['user']['screen_name'])
        tweets_queue.task_done()

if __name__ == '__main__':
    Thread(target=stream_tweets, args=(tweet_queue,), daemon=True).start()

    process_tweets(tweet_queue)