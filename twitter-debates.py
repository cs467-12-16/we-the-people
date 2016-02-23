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
    logging.basicConfig(filename='debates.log', level=logging.INFO)

    count = 14
    last_id = 699284980099387393
    while count < 1000:
        try:
            tweets = api.search(q='#DemDebate OR #GOPDebate OR #DemTownHall OR #GOPTownHall', rpp=100, since_id=last_id)
            if len(tweets) > 0:
                tweetJson = dict()
                with open('test/d' + str(count) + '.json', 'w') as jsonfile:
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