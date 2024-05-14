import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

"""Please change the path"""
# file_path = '/home/ekagra/Desktop/Study/IMECE/visualization/corruption-testing/results/CIFAR10/WideResNet_28_4/Clever vs. PGD-paperversion/config9_standard_eps_0.0_False_run_0_adversarial_distances.csv'
file_path = '/home/ekagra/Desktop/Study/IMECE/visualization/corruption-testing/results/CIFAR10/WideResNet_28_4/Clever vs. PGD-paperversion/config2_run_0_adversarial_distances.csv'

data = pd.read_csv(file_path, sep=';', decimal=',')

norm = 2    # np.inf, 1

clever_score_linf = data[f'{norm}-norm-Clever-1024-samples'].tolist()
adv_dist_pgd = data[f'{norm}-norm-PGD-dist'].tolist()
adv_dist_sec_att = data[f'{norm}-norm-sec-att-dist'].tolist()
indices = data.index.tolist()

min_adv_dist = []
color_adv = []
labels = []

for i, dist in enumerate(adv_dist_pgd):
    if dist<adv_dist_sec_att[i]:
        min_adv_dist.append(dist)
        color_adv.append('blue')
        labels.append('Adversarial Distance (PGD)')
    else:
        min_adv_dist.append(adv_dist_sec_att[i])
        color_adv.append('green')
        labels.append('Adversarial Distance (Second attack)')

colors = ['red' if adv < clv else 'black' for adv, clv in zip(min_adv_dist, clever_score_linf)]

plt.figure(figsize=(4.69, 2.17))
plt.scatter(indices, min_adv_dist, alpha=0.7, label=labels, s=2, c=color_adv)
plt.scatter(indices, clever_score_linf, alpha=0.7, label=labels, s=2, c=colors)

# Create and save the legend as a separate image
markersize = 20

legend_elements = [
    mlines.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=markersize, label='Adversarial Distance (PGD)'),
    mlines.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=markersize, label='Adversarial Distance (Second attack)'),
    mlines.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=markersize, label='Clever Score $\geq$ Adversarial Distance'),
    mlines.Line2D([0], [0], marker='o', color='w', markerfacecolor='black', markersize=markersize, label='Clever Score $<$ Adversarial Distance')
]

fig_legend = plt.figure(figsize=(4.69, 2.17))
ax_legend = fig_legend.add_subplot(111)
ax_legend.legend(handles=legend_elements, loc='center', ncol=4, frameon=False, fontsize=40)
ax_legend.axis('off')

fig_legend.savefig('/home/ekagra/Desktop/Study/IMECE/visualization/adversarial-distance-estimation/visualizations/legend.pdf', bbox_inches='tight', pad_inches=0.1)
plt.close(fig_legend)


plt.xlabel('Image ID', fontsize=14)
plt.ylabel('L$_2$ Distance', fontsize=14)
plt.tight_layout()
plt.savefig(f'/home/ekagra/Desktop/Study/IMECE/visualization/adv_vs_cl_robust_l{norm}_1024_500.pdf')
# plt.savefig(f'/home/ekagra/Desktop/Study/IMECE/visualization/adv_vs_cl_standard_l{norm}_1024_500.pdf')
plt.show()