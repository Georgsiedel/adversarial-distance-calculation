import matplotlib.pyplot as plt
import json

# json_file = '/home/ekagra/Desktop/Study/IMECE/visualization/pgd_vs_en_l1.json'
# json_file = '/home/ekagra/Desktop/Study/IMECE/visualization/pgd_vs_cw_l2.json'
json_file = '/home/ekagra/Desktop/Study/IMECE/visualization/pgd_vs_hsj_linf.json'

with open(json_file, 'r') as f:
    data = json.load(f)

indices = list(range(len(data['projected_gradient_descent']['runtime'])))

plt.figure(figsize=(4.69, 2.87))
ax = plt.gca()

attack_types = data.keys()
colors = ['blue', 'red', 'black', 'green']

for i, attack_type in enumerate(attack_types):
    ax.plot(indices, data[attack_type]['adversarial_distance'], label=" ".join(attack_type.split('_')).title(), linewidth=2, color=colors[i])
    # ax.plot(indices, data[attack_type]['runtime'], label=" ".join(attack_type.split('_')).title(), linewidth=2, color=colors[i])
ax.grid(True, which='major', linestyle='-', color='gray', linewidth=0.1)
ax.set_axisbelow(True)
ax.set_xlabel('Image ID', fontsize=8)
ax.set_ylabel('Adversarial Distance [$L_2$]', fontsize=8)
# ax.set_ylabel('Runtime [$seconds$]', fontsize=8)
ax.tick_params(axis='both', labelsize=8)
ax.legend(fontsize=7)
ax.set_xticks(indices)
ax.set_yscale('log')
plt.tight_layout()

# plt.savefig('/home/ekagra/Desktop/Study/IMECE/visualization/pgd_vs_hsj_linf_runtime.pdf')
# plt.savefig('/home/ekagra/Desktop/Study/IMECE/visualization/pgd_vs_cw_l2_runtime.pdf')
# plt.savefig('/home/ekagra/Desktop/Study/IMECE/visualization/pgd_vs_en_l1_runtime.pdf')
plt.show()
