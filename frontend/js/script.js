$(document).ready(function() {
  var tweetInfooo
  var filteredByHillary
  
  loadJSON('d100', function(data) {
    tweetInfooo = tweetInfo(data.tweets)
    filteredByHillary = filterByHashtag(data.tweets, 'Hillary')
    console.log(tweetInfooo)
    console.log(filteredByHillary)
  })

})

var loadJSON = function(dataToLoad, callback) {
  $.ajax({
    method: 'GET',
    url: './json/twitter-data/' + dataToLoad + '.json'
  }).done(function(res) {
    callback(res)
  })
}