import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

json_file = '/home/ekagra/Desktop/Study/IMECE/visualization/all_attacks_l2.json'

nomenclature_mapping = {
    'carlini_wagner_linf': 'CW',
    'carlini_wagner_l2': 'CW',
    'deep_fool': 'DeepFool',
    'elastic_net': 'ElasticNet',
    'fast_gradient_method': 'FGSM$_{minimal}$',
    'hop_skip_jump': 'HSJ',
    'newton_fool': 'NewtonFool',
    'projected_gradient_descent': 'PGD'
}

# Load JSON data
with open(json_file, 'r') as f:
    data = json.load(f)

# Prepare data
attack_types = list(data.keys())
mean_adv_distances = [np.mean(data[at]["adversarial_distance"]) for at in attack_types]
total_runtimes = [np.sum(data[at]["runtime"]) for at in attack_types]
# print(attack_types)
# Create DataFrame
df = pd.DataFrame({
    'Attack Method': attack_types,
    'Mean Adv Dist': mean_adv_distances,
    'Total Runtime': total_runtimes
})

# Sort DataFrame by 'Mean Adv Dist'
df.sort_values(by='Mean Adv Dist', ascending=False, inplace=True)
df['Attack Method'] = df['Attack Method'].map(nomenclature_mapping)

# Plotting
fig, ax1 = plt.subplots(figsize=(4.69, 3))
ind = np.arange(len(df))  # the x locations for the groups
width = 0.35  # width of the bars

# Plot Mean Adversarial Distance
ax1.bar(ind - width/2, df['Mean Adv Dist'], width, label='Mean Adv Dist', color='blue')
ax1.set_ylabel('Mean Adversarial Distance', color='blue')
ax1.set_xticks(ind)
ax1.set_xticklabels(df['Attack Method'], rotation=30)
ax1.tick_params(axis='both', labelsize=8)

# Create twin axis for runtime
ax2 = ax1.twinx()
ax2.bar(ind + width/2, df['Total Runtime'], width, label='Total Runtime', color='red')
ax2.set_ylabel('Total Runtime [seconds]', color='red')
ax2.tick_params('both', labelsize=9)

# Adding a legend and layout adjustment
# fig.legend(loc='upper right', bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
plt.tight_layout()

# Save and show plot
# plt.savefig('/home/ekagra/Desktop/Study/IMECE/visualization/attacks_comparison_bar_l1.pdf')
# plt.show()

# print(f'Attack: {df["Attack Method"]}\tMean Adv Dist: {df["Mean Adv Dist"]}')