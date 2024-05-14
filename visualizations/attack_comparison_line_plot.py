import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

norm = 2

json_file = f'/home/ekagra/Desktop/Study/IMECE/visualization/all_attacks_l{norm}.json'


with open(json_file, 'r') as f:
    data = json.load(f)

indices = list(range(len(data['projected_gradient_descent']['runtime'])))

attack_types = list(data.keys())

plt.figure(figsize=(4.69, 2.87))
ax = plt.gca()
# colors = ['blue', 'red']
for i, attack_type in enumerate(attack_types):
    # ax.plot(indices, data[attack_type]['adversarial_distance'], label=" ".join(attack_type.split('_')).title(), linewidth=2)
    ax.plot(indices, data[attack_type]['runtime'], label=" ".join(attack_type.split('_')).title(), linewidth=2)
ax.grid(True, which='major', linestyle='-', color='gray', linewidth=0.1)
ax.set_axisbelow(True)
ax.set_xlabel('Image ID', fontsize=8)
# ax.set_ylabel('Distance', fontsize=8)
ax.set_ylabel('Runtime', fontsize=8)
ax.tick_params(axis='both', labelsize=8)
# ax.legend(loc='upper right', fontsize=7)
ax.set_yscale('log')
ax.set_xticks(indices)
plt.tight_layout()

# plt.savefig(f'/home/ekagra/Desktop/Study/IMECE/visualization/all_attacks_L{norm}.pdf')
plt.savefig(f'/home/ekagra/Desktop/Study/IMECE/visualization/all_attacks_L{norm}_runtime.pdf')
plt.show()