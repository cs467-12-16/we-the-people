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
