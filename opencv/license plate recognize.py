# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:12:30 2018

@author: hp
"""

key="ed4ff5af-88ef-4036-a05f-aeadffb8e57c"

from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient(key, "v1") #apikey

params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
#params = {'file': 'E:/abcd.mp4', 'source_location': 'GB'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print (response)

#dump data in a json file
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)