import { readFile, writeFile } from 'fs'
import async from 'async'
import R from 'ramda'

// create a list of all files in twitter-data
let files = []
for (let i = 0; i < 1000; i++) {
  // d13.json is empty, so this is a hacky workaround
  if (i !== 13) {
    const filename1 = './json/twitter-data/d' + i + '.json'
    files.push(filename1)
  }
  const filename2 = './json/twitter-data/t' + i + '.json'
  files.push(filename2)
}

function read(file, callback) {
  readFile(file, 'utf8', callback)
}

async.map(files, read, (err, results) => {
  if (err) throw err

  results = results.map(file => JSON.parse(file))
  const tweets = R.flatten(results.map(result => result.tweets))
  const tweetsSample = tweets.slice(0, 10)

  writeFile('./json/twitter-data-merged/twitter-data-merged-sample.json', JSON.stringify(tweetsSample), (err) => {
    if (err) throw err
    console.log('sample data successfully merged!')
  })

  writeFile('./json/twitter-data-merged/twitter-data-merged.json', JSON.stringify(tweets), (err) => {
    if (err) throw err
    console.log('data successfully merged!')
  })
})
