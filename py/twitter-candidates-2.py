import tweepy
import logging, time, datetime
import csv, json

consumer_key = ""
consumer_secret = ""

access_token = ""
access_token_secret = ""

def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    logging.basicConfig(filename='queries2.log', level=logging.INFO)

    count = 0
    last_id = 699374318225113088
    while count < 1000:
        try:
            tweets = api.search(q='hillary OR clinton OR donald OR trump OR marco OR rubio OR bernie OR sanders', rpp=100, since_id=last_id)
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
    main()