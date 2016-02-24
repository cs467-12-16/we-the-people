import json, os

candidates = ['bernie sanders', 'donald trump', 'hillary clinton', 'marco rubio', 'ben carson', 'john kasich']
issues = ['tuition', 'immigration', 'economy', 'healthcare']

tweet_totals_dict = { 'name': 'all', 'size': 0, 'children': []}

for issue in issues:
    issue_obj = {'name': issue, 'size': 0, 'children': []}
    for candidate in candidates:
        candidate_obj = {'name': candidate, 'size': 0}
        issue_obj['children'].append(candidate_obj)
    issue_obj['children'].append({ 'name': 'unknown', 'size': 0 })
    tweet_totals_dict['children'].append(issue_obj)

unknown_issue_obj = {'name': 'unknown', 'size': 0, 'children': []}
for candidate in candidates:
    candidate_obj = {'name': candidate, 'size': 0}
    unknown_issue_obj['children'].append(candidate_obj)
unknown_issue_obj['children'].append({ 'name': 'unknown', 'size': 0 })
tweet_totals_dict['children'].append(unknown_issue_obj)

count = 0
for count in range(1000):
    index = str(count)
    t_file_name = '../json/twitter-data/t' + index + '.json'
    d_file_name = '../json/twitter-data/d' + index + '.json'
    data = []
    with open(t_file_name) as t_file:
        if os.path.getsize(t_file_name) > 0:
            dataT = json.load(t_file)
            for tweet in dataT['tweets']:
                data.append(tweet)
    with open(d_file_name) as d_file:
        if os.path.getsize(d_file_name) > 0:
            dataD = json.load(d_file)
            for tweet in dataD['tweets']:
                data.append(tweet)
    for t in range(len(data)):
        tweet = data[t]
        tweet_totals_dict['size'] += 1
        text = tweet['text'].lower()
        iindex = -1
        cindex = -1
        for i in issues:
            try:
                if text.index(i) >= 0:
                    iindex = next(index for (index, d) in enumerate(tweet_totals_dict['children']) if d['name'] == i)
                    tweet_totals_dict['children'][iindex]['size'] += 1
            except ValueError:
                continue
        if iindex == -1:
            iindex = next(index for (index, d) in enumerate(tweet_totals_dict['children']) if d['name'] == 'unknown')
            tweet_totals_dict['children'][iindex]['size'] += 1
        for c in candidates:
            try:
                if text.index(c) >= 0:
                    cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == c)
                    tweet_totals_dict['children'][iindex]['children'][cindex]['size'] += 1
            except ValueError:
                continue
        if cindex == -1:
            cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == 'unknown')
            tweet_totals_dict['children'][iindex]['children'][cindex]['size'] += 1

with open('json/totals-tweets.json', 'w') as jsonfile:
    json.dump(tweet_totals_dict, jsonfile)