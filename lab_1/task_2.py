import matplotlib.pyplot as plt
import pandas as pd
import lab_1.config


def interval_variation_series(data, count):
    df = pd.Series(data)
    keys = df.unique()
    keys.sort()
    d = df.groupby(pd.cut(df, list(map(lambda x: x / 100.0,
                                  range(int(min(data) * 100) - 1, int(max(data) * 100) + 1,
                                        int(count * 100)))))).count()
    print(d)
    d.plot(kind='bar', grid=True)
    plt.savefig("./img2.png")
    plt.show()


if __name__ == '__main__':
    data = [12, 6, 8, 6, 10, 11, 7, 10, 12, 8, 7, 7, 6, 7, 8, 6, 11, 9, 11,
            9, 10, 11, 9, 10, 7, 8, 8, 8, 11, 9, 8, 7, 5, 9, 7, 7, 14, 11,
            9, 8, 7, 4, 7, 5, 5, 10, 7, 7, 5, 8, 10, 10, 15, 10, 10, 13, 12,
            11, 15, 6]
    interval_variation_series(data, 2)
