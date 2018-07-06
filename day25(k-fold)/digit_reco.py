from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("36b065f3-7ce8-4872-8066-4b9e6d64b659", "v1") #apikey

#https://api.havenondemand.com/1/api/async/ocrdocument/v1

params = {'file': 'convo-1-text-8.png'} ## or if using a local file


response_async = client.post_request(params, 'ocrdocument', async=True)

jobID = response_async['jobID']
print(jobID)

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print(response)

#dump data in a json file
with open('digitreco.json', 'w') as outfile:
    json.dump(response, outfile)