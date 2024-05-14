import pandas as pd

file_path = '/home/ekagra/Desktop/Study/IMECE/visualization/corruption-testing/results/CIFAR10/WideResNet_28_4/config9_standard_eps_0.0_False_run_0_adversarial_distances.csv'
data = pd.read_csv(file_path)
print(data.head(1))