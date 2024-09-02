import pandas as pd
import json
import os
import numpy as np

csv_file_path = '/home/ekagra/Documents/GitHub/adversarial-distance-estimation/data/paper_data/adv_dist_vs_clever_robust_500.csv'
json_file_path = '/home/ekagra/Documents/GitHub/adversarial-distance-estimation/data/paper_data/adv_dist_vs_clever_robust_500.json'

# You can switch between different norms by modifying the columns and norm variable
norm = np.inf

columns = [f'{norm}-norm-PGD-dist',
           f'{norm}-norm-sec-att-dist',
           f'{norm}-norm-Clever-5-samples',
           f'{norm}-norm-Clever-20-samples',
           f'{norm}-norm-Clever-100-samples',
           f'{norm}-norm-Clever-1024-samples']

# Read the data from the CSV file
data = pd.read_csv(csv_file_path, sep=';', decimal=',')

# Extract the relevant columns
adversarial_distance_pgd = data[columns[0]].values
adversarial_distance_sec_att = data[columns[1]].values
clever_config_5 = data[columns[2]].values
clever_config_20 = data[columns[3]].values
clever_config_100 = data[columns[4]].values
clever_config_1024 = data[columns[5]].values

# Create the new data dictionary for the current norm
new_data_dict = {}
new_data_dict[f'{norm}'] = {
    'adversarial_distance_pgd': adversarial_distance_pgd.tolist(),
    'adversarial_distance_second_attack': adversarial_distance_sec_att.tolist(),
    'clever_score': {
        '5-5': clever_config_5.tolist(),
        '10-20': clever_config_20.tolist(),
        '50-100': clever_config_100.tolist(),
        '500-1024': clever_config_1024.tolist(),
    },
    'max_adversarial_distance': 0.0498082638
}

# Check if the JSON file already exists
if os.path.exists(json_file_path):
    # Load existing data from the JSON file
    with open(json_file_path, 'r') as json_file:
        existing_data = json.load(json_file)
else:
    # If the file doesn't exist, create an empty dictionary
    existing_data = {}

# Update the existing data with the new data
existing_data.update(new_data_dict)

# Save the updated data back to the JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(existing_data, json_file, indent=4)
