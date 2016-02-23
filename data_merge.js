import { readFile, writeFile } from 'fs'
import async from 'async'

let files = []
for (let i = 0; i < 1000; i++) {
  const filename1 = './json/twitter-data/d' + i + '.json'
  const filename2 = './json/twitter-data/t' + i + '.json'
  files.push(filename1)
  files.push(filename2)
}

function read(file, callback) {
  readFile(file, 'utf8', callback)
}

async.map(files, read, (err, results) => {
  if (err) throw err
  console.log(JSON.parse(results[0]).entities)
  results = results.map(file => JSON.parse(file))
  console.log(results[0].count)
  // writeFile('./json/twitter-data-merged.json', JSON.stringify(results), (err) => {
  //   if (err) throw err
  // })
})