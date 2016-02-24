/**
 * Maps all tweets to extract the relevant info
 * @param  {Array} tweets [the list of all tweets]
 * @return {Array}        [a list containing just the relevant information needed]
 */
function tweetInfo(tweets) {
  return tweets.map(tweet => ({
    text: tweet.text,
    hashtags: tweet.entities.hashtags.map(hashtag => hashtag.text),
    location: tweet.user.location,
    timestamp: tweet.created_at
  }))
}

/**
 * Filters and returns tweets given a hashtag
 * @param  {Array}  tweets  [the list of all tweets]
 * @param  {String} hashtag [hashtag to filter on]
 * @return {Array}          [filtered tweets]
 */
function filterByHashtag(tweets, hashtag) {
  return tweets.filter(tweet => {
    // check if the hashtag we're looking for is contained in the tweet's hashtags array
    const text = tweet.entities.hashtags.map(hashtag => hashtag.text)
    return text.includes(hashtag)
  })
}

export default {
  tweetInfo,
  filterByHashtag
}