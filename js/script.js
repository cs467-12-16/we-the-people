/**
 * Maps all tweets to extract the relevant info
 * @param  {Array} tweets [the list of all tweets]
 * @return {Array}        [a list containing just the relevant information needed]
 */
var tweetInfo = function(tweets) {
  var mapped = tweets.map(function(tweet) {
    return {
      text: tweet.text,
      hashtags: tweet.entities.hashtags.map(function(hashtag) { return hashtag.test }),
      location: tweet.user.location,
      timestamp: tweet.created_at
    }
  })
}

/**
 * Filters and returns tweets given a hashtag
 * @param  {Array}  tweets  [the list of all tweets]
 * @param  {String} hashtag [hashtag to filter on]
 * @return {Array}          [filtered tweets]
 */
var filterByHashtag = function(tweets, hashtag) {
  return tweets.filter(function(tweet) {
    // check if the hashtag we're looking for is contained in the tweet's hashtags array
    return !!~tweet.entities.hashtags.indexOf(hashtag)
  })
}

