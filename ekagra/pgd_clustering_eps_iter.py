import matplotlib.pyplot as plt
import json

# json_file_0 = '/home/ekagra/Desktop/Study/IMECE/visualization/pgd_standard_eps_iter_3e-1.json'
json_file_1 = '/home/ekagra/Desktop/Study/IMECE/visualization/pgd_standard_eps_iter_3e-2.json'
json_file_2 = '/home/ekagra/Desktop/Study/IMECE/visualization/pgd_standard_eps_iter_3e-3.json'
json_file_3 = '/home/ekagra/Desktop/Study/IMECE/visualization/pgd_standard_eps_iter_3e-4.json'

json_files = [json_file_1, json_file_2, json_file_3]
adversarial_distances_dict = {}

for i, json_file in enumerate(json_files):
    with open(json_file, 'r') as f:
        data = json.load(f)

    indices = list(range(len(data['projected_gradient_descent']['runtime'])))
    adversarial_distances_dict[i] = data['projected_gradient_descent']['adversarial_distance']
    
# plt.figure(figsize=(4.69, 4.71))
# ax = plt.gca()
fig, ax = plt.subplots(1, 3, figsize=(4.69, 1.57))
ax[0].scatter(indices, adversarial_distances_dict[0], s=5, c='blue')
ax[0].set_title('eps_iter = 0.03', fontsize=8)
ax[0].set_xlabel('ImageID', fontsize=8)
ax[0].set_ylabel('L$_2$ Distance', fontsize=8)
ax[0].tick_params(axis='both', labelsize=8)
ax[1].scatter(indices, adversarial_distances_dict[1], s=5, c='blue')
ax[1].set_title('eps_iter = 0.003', fontsize=8)
ax[1].set_xlabel('ImageID', fontsize=8)
# ax[1].set_ylabel('Linf Distance', fontsize=6)
ax[1].tick_params(axis='both', labelsize=6)
ax[2].scatter(indices, adversarial_distances_dict[2], s=5, c='blue')
ax[2].set_title('eps_iter = 0.0003', fontsize=8)
ax[2].set_xlabel('ImageID', fontsize=8)
# ax[2].set_ylabel('Linf Distance', fontsize=6)
ax[2].tick_params(axis='both', labelsize=6)
plt.tight_layout()
plt.savefig('/home/ekagra/Desktop/Study/IMECE/visualization/pgd_standard_eps_iter.pdf')
plt.show()

