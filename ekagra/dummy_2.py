import numpy as np
import json

json_path = '/home/ekagra/Desktop/Study/IMECE/visualization/clever_score_robust_l2.json'

with open(json_path, 'r') as f:
    data = json.load(f)

for key in data.keys():
    sum_runtime = np.sum(data[key]['runtime'])
    print(f'Config: {key}\truntime: {sum_runtime:.3f}s')