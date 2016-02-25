import json, os

candidates_first = ['bernie', 'donald', 'hillary', 'marco', 'ben', 'john', 'ted', 'jeb']
candidates_last = ['sanders', 'trump', 'clinton', 'rubio', 'carson', 'kasich', 'cruz', 'bush']

issues = ['tuition', 'immigration', 'economy', 'healthcare', 'poverty', 'security']

def initialize_dict():
    dictionary = { 'name': 'all', 'size': 0, 'children': []}
    for issue in issues:
        issue_obj = {'name': issue, 'size': 0, 'children': []}
        for candidate in candidates_last:
            candidate_obj = {'name': candidate, 'size': 0}
            issue_obj['children'].append(candidate_obj)
        issue_obj['children'].append({'name': 'unknown', 'size': 0, 'children': []})
        dictionary['children'].append(issue_obj)

    unknown_issue_obj = {'name': 'unknown', 'size': 0, 'children': []}
    for candidate in candidates_last:
        candidate_obj = {'name': candidate, 'size': 0}
        unknown_issue_obj['children'].append(candidate_obj)
    unknown_issue_obj['children'].append({'name': 'unknown', 'size': 0, 'children': []})
    dictionary['children'].append(unknown_issue_obj)
    return dictionary

tweet_totals_dict = initialize_dict()
facebook_totals_dict = initialize_dict()
totals_dict = initialize_dict()

# Twitter Data Handling
count = 0
indices = ['t', 'd', 'c']
for count in range(1000):
    index = str(count)
    data = []
    for k in range(len(indices)):
        file_name = '../json/twitter-data/' + indices[k] + index + '.json'
        with open(file_name) as data_file:
            if os.path.getsize(file_name) > 0:
                d = json.load(data_file)
                for tweet in d['tweets']:
                    data.append(tweet)
    for t in range(len(data)):
        tweet = data[t]
        tweet_totals_dict['size'] += 1
        totals_dict['size'] += 1
        text = tweet['text'].lower()
        iindex = -1
        cindex = -1
        for i in issues:
            try:
                if text.index(i) >= 0:
                    iindex = next(index for (index, d) in enumerate(tweet_totals_dict['children']) if d['name'] == i)
                    tweet_totals_dict['children'][iindex]['size'] += 1
                    totals_dict['children'][iindex]['size'] += 1
            except ValueError:
                continue
        if iindex == -1:
            iindex = next(index for (index, d) in enumerate(tweet_totals_dict['children']) if d['name'] == 'unknown')
            tweet_totals_dict['children'][iindex]['size'] += 1
            totals_dict['children'][iindex]['size'] += 1
        for l in candidates_last:
            try:
                if text.index(l) >= 0:
                    cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == l)
                    tweet_totals_dict['children'][iindex]['children'][cindex]['size'] += 1
                    totals_dict['children'][iindex]['children'][cindex]['size'] += 1
            except ValueError:
                continue
        for f in range(len(candidates_first)):
            fn = candidates_first[f]
            try:
                if text.index(fn) >= 0:
                    cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == candidates_last[f])
                    tweet_totals_dict['children'][iindex]['children'][cindex]['size'] += 1
                    totals_dict['children'][iindex]['children'][cindex]['size'] += 1
            except ValueError:
                continue
        if cindex == -1:
            cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == 'unknown')
            tweet_totals_dict['children'][iindex]['children'][cindex]['size'] += 1
            totals_dict['children'][iindex]['children'][cindex]['size'] += 1

# Facebook Data Handling
candidates = ['clinton', 'sanders', 'trump']
for candidate in candidates:
    file_name = '../json/facebook-data/' + candidate + '.json'
    with open(file_name) as data_file:
        data = json.load(data_file)[0]
        for comment in data['comments']['data']:
            text = str(comment['message'].encode('ascii', 'ignore')).lower()
            iindex = -1
            cindex = -1
            facebook_totals_dict['size'] += 1
            totals_dict['size'] += 1
            for i in issues:
                try:
                    if text.index(i) >= 0:
                        iindex = next(index for (index, d) in enumerate(tweet_totals_dict['children']) if d['name'] == i)
                        facebook_totals_dict['children'][iindex]['size'] += 1
                        totals_dict['children'][iindex]['size'] += 1
                except ValueError:
                    continue
            if iindex == -1:
                iindex = next(index for (index, d) in enumerate(tweet_totals_dict['children']) if d['name'] == 'unknown')
                facebook_totals_dict['children'][iindex]['size'] += 1
                totals_dict['children'][iindex]['size'] += 1
            for l in candidates_last:
                try:
                    if text.index(l) >= 0:
                        cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == l)
                        facebook_totals_dict['children'][iindex]['children'][cindex]['size'] += 1
                        totals_dict['children'][iindex]['children'][cindex]['size'] += 1
                except ValueError:
                    continue
            for f in range(len(candidates_first)):
                fn = candidates_first[f]
                try:
                    if text.index(fn) >= 0:
                        cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == candidates_last[f])
                        facebook_totals_dict['children'][iindex]['children'][cindex]['size'] += 1
                        totals_dict['children'][iindex]['children'][cindex]['size'] += 1
                except ValueError:
                    continue
            if cindex == -1:
                cindex = next(index for (index, d) in enumerate(tweet_totals_dict['children'][iindex]['children']) if d['name'] == 'unknown')
                facebook_totals_dict['children'][iindex]['children'][cindex]['size'] += 1
                totals_dict['children'][iindex]['children'][cindex]['size'] += 1

with open('../json/twitter-data-filtered/totals-tweets.json', 'w') as jsonfile:
    json.dump(tweet_totals_dict, jsonfile)

with open('../json/facebook-data-filtered/totals-comments.json', 'w') as jsonfile:
    json.dump(facebook_totals_dict, jsonfile)

with open('../json/overview.json', 'w') as jsonfile:
    json.dump(totals_dict, jsonfile)