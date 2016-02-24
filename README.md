# We the People
We the People is a visualization of Twitter and Facebook data related to the upcoming elections.

## Group Members
Group 12
- Ran Meng
- Varun Munjeti
- Emily Chao

## d3 CDN
To add to the top or bottom of the HTML file with the visualization
```
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.16/d3.min.js" charset="utf-8"></script>
```

## Notes
### Twitter Data Processing
#### Setup
In order to run these scripts, you need to have node.js installed. Then `npm install` to install all dependencies.

#### Building and Running
The source of these scripts are in `./scripts` but will need to be transpiled before running. In order to do that, run `npm run build`. You have to run this command every time you make changes to any source files. This will produce executable code inside `./dist`. You can then run the scripts with `node dist/<filename>`, assuming you are in the root directory.

#### File I/O
`json/twitter-data` contains the original data

`json/twitter-data-merged` contains the concatenation of everything from the original data

`json/twitter-data-filtered` contains the filtered tweet data, which is what we should use in the frontend.

Note: `json/twitter-data-merged/twitter-data-merged.json` is too large of a file to commit. I added it to the `.gitignore`, but in order to create the file locally, run `node dist/data_merge.js`.

#### Creating and Using Filters
The source for the filters are in `scripts/utils.js`. New filters and other utility functions should go here, but they should be utilized to actually create filitered data in a separate file, such as `scripts/create_filtered_data.js`. If newly created filtered data is necessary for the frontend, output it to `./json/twitter-data-filtered`.

## Workflow
We are going to try to implement the Candidate-Issue view and the Overview, in that order, for 3 candidates: Bernie, Hillary, and Trump.

Todo for Data:
- Use Twitter API - #GOPDebate, #DemDebate, #FeelTheBern, #Hillary, #Trump2016
- Scrape Facebook pages - Hillary Clinton's, Bernie Sanders', and Donald Trump's - grab comments, from the comments grab profile links, and then use Profile API from Graph API to get information about the person
- Run all of the data through AlchemyAPI - TextGetTextSentiment, Keyword Extraction Sentiment Targeting (all under Sentimenet Analysis). There's also a separate section for just Keyword Extraction.

Todo for Candidate-Issue:
- Design the stream
- Show the sentiment slider.
- Do the time slider.
- Build the histogram for Geographic location (extract from Twitter and Facebook and use Reverse Geocoding API from Google Maps?)
- Configure additional filters for histogram based on Facebook extracted data.

Todo for Overview:
- Design bubbles based on time and candidate + issue first.
- If have time, configure filters.

We need to vote on either 2-space or 4-space tabbing.
