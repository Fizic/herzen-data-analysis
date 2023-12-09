import matplotlib.pyplot as plt
import pandas as pd
import config


def discrete_variation_series(data):
    s = pd.Series(data)
    keys = s.unique()
    keys.sort()
    ans = s.value_counts(sort=True)[keys]
    print(ans)
    ans.plot(kind='bar', grid=True)
    plt.savefig("./img1.png")
    plt.show()


if __name__ == '__main__':
    data = [4, 0, 3, 4, 1, 0, 3, 1, 0, 4, 0, 0, 3, 1, 0, 1, 1, 3, 2, 3, 1, 2, 1, 2]
    discrete_variation_series(data)
