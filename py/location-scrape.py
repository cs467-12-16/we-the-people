import json

bins = ['west', 'midwest', 'northeast', 'southeast', 'southwest', 'international', 'other']
dictionary = []
for b in bins:
    dictionary.append({'bin': b, 'size': 0})

with open('../json/location-sample.json') as jsonfile:
    data = json.load(jsonfile)
    for i in range(len(data)):
        if data[i].get('location_bin') is None:
            cindex = next(index for (index, d) in enumerate(dictionary) if d['bin'] == 'other')
        else:
            cindex = next(index for (index, d) in enumerate(dictionary) if d['bin'] == data[i]['location_bin'])
        dictionary[cindex]['size'] += 1

with open('../json/location-d3.json', 'w') as jsonfile:
    json.dump(dictionary, jsonfile)