import numpy as np
from mlchain.client import Client

model = Client(api_address='http://localhost:5000').model()
wf = '/home/pdd/Desktop/sandbox/AI_interview/sample_wav/sample.wav'
result = model.get_reaction_score(wf)
print(result)  