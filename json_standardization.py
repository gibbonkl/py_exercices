import pandas as pd 
import json

data = []

in_file = 'taxi_small.json'
out_file = 'taxi-converted.json'

# reading lines and appending into an array
with open(in_file, 'r') as f:
    for line in f:
        #if (line.find("{") > -1):
            entry = line[line.find("{"):line.rfind("}")]+"}"
            data.append(json.loads(entry))

# converting the array to json format and saving into a file
with open(out_file, 'w') as f:
    f.write(json.dumps(data))

# converting the array to csv format and saving into a file
pd.DataFrame(data).to_csv('taxi-converted.csv', index = False)

# converting the array to pandas json format and saving into a file
pd.DataFrame(data).to_json('taxi-converted_pd.json')