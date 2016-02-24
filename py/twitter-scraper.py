import tweepy
import logging, time, datetime
import csv, json

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

logging.basicConfig(filename='queries.log', level=logging.INFO)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def fetch_tweets(query, last_id):
    count = 0
    while count < 1000:
        try:
            tweets = api.search(q=query, rpp=100, since_id=last_id)
            tweetJson = dict()
            if len(tweets) > 0:
                with open('testC2/c' + str(count) + '.json', 'w') as jsonfile:
                    tweetJson['count'] = len(tweets)
                    tweetJson['tweets'] = [tweet._json for tweet in tweets]
                    last_id = tweets[-1].id
                    json.dump(tweetJson, jsonfile)
                    logging.info('json dumped ' + str(count))
                count += 1
        except tweepy.TweepError:
            logging.info('sleeping')
            time.sleep(15*60)

if __name__ == '__main__':
    last_id = 699374318225113088
    fetch_tweets('hillary OR clinton OR donald OR trump OR marco OR rubio OR bernie OR sanders', last_id)
    fetch_tweets('#hillary OR #feelthebern OR #trump2016 OR tuition OR healthcare OR economy OR immigration', last_id)
    fetch_tweets('#DemDebate OR #GOPDebate OR #DemTownHall OR #GOPTownHall', last_id)
    fetch_tweets('hillary clinton OR donald trump OR marco rubio OR bernie sanders', last_id)