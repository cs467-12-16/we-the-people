import utils from './utils'
import { readFile } from 'fs'

console.log(utils.filterByHashtag)

const filePath = './json/twitter-data-merged/twitter-data-merged-sample-pretty.json'
readFile(filePath, 'utf8', (err, result) => {
  result = JSON.parse(result)
  const filtedByHillary2016 = utils.filterByHashtag(result, 'Hillary2016')
  const tweetInfoFiltered = utils.tweetInfo(filtedByHillary2016)
  console.log(tweetInfoFiltered)
})