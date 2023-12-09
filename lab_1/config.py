from matplotlib import pyplot as plt

large = 22
med = 16
small = 12
params = {'legend.fontsize': small,
          'figure.figsize': (20, 20),
          'axes.labelsize': large,
          'axes.titlesize': large,
          'xtick.labelsize': 25,
          'ytick.labelsize': 40,
          'figure.titlesize': large}
plt.rcParams.update(params)