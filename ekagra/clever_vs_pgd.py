import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path_1 = '/home/ekagra/Desktop/Study/IMECE/visualization/corruption-testing/results/CIFAR10/WideResNet_28_4/Clever vs. PGD -clever-eps-0.1/config2_adversarial_distance_5-5.csv'
file_path_2 = '/home/ekagra/Desktop/Study/IMECE/visualization/corruption-testing/results/CIFAR10/WideResNet_28_4/Clever vs. PGD -clever-eps-0.1/config2_adversarial_distance_20-10.csv'
file_path_3 = '/home/ekagra/Desktop/Study/IMECE/visualization/corruption-testing/results/CIFAR10/WideResNet_28_4/Clever vs. PGD -clever-eps-0.1/config2_adversarial_distance_100-50.csv'
file_path_4 = '/home/ekagra/Desktop/Study/IMECE/visualization/corruption-testing/results/CIFAR10/WideResNet_28_4/Clever vs. PGD -clever-eps-0.1/config2_adversarial_distance_1024-500.csv'

file_paths = [file_path_1,
              file_path_2,
              file_path_3,
              file_path_4]

configs = ['5-5',
           '20-10',
           '100-50',
           '1024-500']

mean_adv_distance_list, mean_clever_score_list, proportion_greater_list = [], [], []

# data = pd.read_csv(file_path_1, sep=';', decimal=',')

# for i, file_path in enumerate(file_paths):
#     data = pd.read_csv(file_path, sep=';', decimal=',')

#     adv_distance = data['Adversarial_Distance_sorted']
#     clever_score = data['Clever_Score_sorted_by_Adversarial_Distance']
#     indices = data.index.to_list()

#     colors = ['red' if adv < clv else 'black' for adv, clv in zip(adv_distance, clever_score)]

#     proportion_greater = (clever_score > adv_distance).mean() * 100

#     proportion_greater_list.append(f'{proportion_greater:.2f}')
#     mean_adv_distance_list.append(f'{np.mean(adv_distance):.5f}')
#     mean_clever_score_list.append(f'{np.mean(clever_score):.5f}')

    # plt.figure(figsize=(15, 6))
    # plt.scatter(indices, adv_distance, alpha=0.7, label='Adversarial Distance', s=5)
    # plt.scatter(indices, clever_score, alpha=0.7, label='Clever Score', s=5, c=colors)

    # plt.legend()
    # plt.title(f'Proportion of Clever Scores Greater Than Adversarial Distance: {proportion_greater:.2f}%')
    # plt.tight_layout()
    # plt.show()

# data = {'Config': configs,
#         'Mean Adversarial Distance': mean_adv_distance_list,
#         'Mean Clever Score': mean_clever_score_list,
#         'Proportion': proportion_greater_list
#         }

# df = pd.DataFrame(data)

# df.to_csv('robust_clever.csv', index=False)

# plt.figure(figsize=(4.69, 2.87))
# ax = plt.gca()
# colors = ['blue', 'red', 'black', 'green']
# for i, attack_type in enumerate(attack_types):
# ax.scatter(indices, adv_distance, alpha=0.7, label='Adversarial Distance', s=5)
# ax.scatter(indices, clever_score, alpha=0.7, label='Clever Score', s=5, c=colors)
# ax.grid(True, which='both', linestyle='-', color='gray', linewidth=0.1)
# ax.set_axisbelow(True)
# ax.set_xlabel('Image ID', fontsize=8)
# ax.set_ylabel('Linf Distance', fontsize=8)
# ax.tick_params(axis='both', labelsize=8)
# ax.legend(loc='upper left', fontsize=7)
# # ax.set_xticks(indices)
# plt.tight_layout()

# plt.savefig('/home/ekagra/Desktop/Study/IMECE/visualization/adv_distance_vs_clever_1024_500.pdf')
# plt.show()