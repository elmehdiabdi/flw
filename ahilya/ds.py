import requests
import json

r = requests.get('https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json')
json_data = json.loads(r.text)
print(len(json_data))
counter = 0
for x in json_data:
	file = open('dataset/'+str(counter)+'.json', 'a')
	print(x, type(x))
	file.write(json.dumps(x))
	counter += 1
	file.close()
