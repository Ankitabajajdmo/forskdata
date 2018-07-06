from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("7d047c05-39d5-4b04-8b59-d2fd88e1b13e", "v1") #apikey

#params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
params = {'file': 'Private Number Plates - Cars & Motorbikes for Your Viewing Pleasure.mp4', 'source_location': 'IN'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
print(jobID)

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print(response)

#dump data in a json file
with open('data2.json', 'w') as outfile:
    json.dump(response, outfile)