import matplotlib.pyplot as plt
import lab_1.config

def interval_variation_series(data):
    plt.bar(data.keys(), data.values())
    plt.savefig("./img3.png")
    plt.show()


def interval_variation_series_1(data):
    sums = []
    cc = 0
    for i in data.values():
        cc += i
        sums.append(cc)

    plt.plot(data.keys(), sums)
    plt.savefig("./img3.png")
    plt.show()


if __name__ == '__main__':
    data = {"(0, 5000]": 4, "(0, 7000]": 12, "(0, 10000]": 8, "(0, 15000]": 6}
    interval_variation_series(data)
