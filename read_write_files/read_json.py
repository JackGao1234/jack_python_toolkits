import os
import json
import pandas as pd


path_to_json = 'json/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

jsons_data = pd.DataFrame(columns=['recipe', 'timestamp', 'some_list'])


for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        recipe = json_text['recipe']
        timestamp = json_text['timestamp']
        partial_golden_trace = json_text['some_list']

        jsons_data.loc[index] = [recipe, timestamp, partial_golden_trace]

# now that we have the pertinent json data in our DataFrame let's look at it
print(jsons_data)
