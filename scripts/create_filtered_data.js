import utils from './utils'
import { readFile, writeFile } from 'fs'

// using the entire merged twitter data
const filepathToRead = './json/twitter-data-merged/twitter-data-merged.json'
readFile(filepathToRead, 'utf8', (err, allTweets) => {
  if (err) throw err

  allTweets = JSON.parse(allTweets)
  const allTweetsInfo = utils.tweetInfo(allTweets)

  const filepathToWrite = './json/twitter-data-filtered/all-tweets-info.json'
  writeFile(filepathToWrite, JSON.stringify(allTweetsInfo), err => {
    if (err) throw err
    console.log('all tweets info file successfully written!')
  })
})