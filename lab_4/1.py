import csv
import math
from pylab import rcParams
from matplotlib import pyplot as plt

rcParams['figure.figsize'] = 1920 / 100, 2400 / 100

salaries = [35, 36, 41, 44, 40, 42, 51, 55, 58, 56, 52, 57, 63, 62, 67, 62, 68, 63, 69, 64, 79, 74,
            77, 79, 70, 72, 73, 78, 72, 77, 71, 89, 81, 84, 81, 88, 88, 84, 85, 80, 84, 81, 84, 89,
            83, 91, 91, 93, 92, 96, 91, 97, 92, 91, 91, 97, 97, 96, 93, 95, 106, 100, 107, 104, 100,
            108, 109, 107, 109, 104, 103, 100, 102, 117, 118, 110, 119, 114, 111, 118, 115, 118,
            112, 116, 125, 120, 128, 122, 122, 128, 126, 129, 130, 138, 132, 138, 131, 138, 147,
            142, 143, 142, 140, 158, 157, 151, 166, 162]

# Вариационный ряд
salaries.sort()
var = {}
d = 10
print('x_i'.ljust(20), "m_i")
for sal in range(30, 170, d):
    key = f'[{sal}, {sal + d})'
    val = len(list(filter(lambda x: sal <= x < sal + d, salaries)))
    var[key] = val
    print(key.ljust(20), val)

plt.bar(var.keys(), var.values(), 0.7)
plt.yticks(size=20)
plt.xticks(rotation=90, size=20)
plt.savefig("./img1.png")
plt.show()

# Накопливающийся ряд
for key in range(12):
    pass

print()
n = len(salaries)
print("n:", n)
print("Минимальное значение:", min(salaries))
print("Максимальное значение:", max(salaries))


def func1(xi, mi):
    x_ = 0
    for x, m in zip(xi, mi):
        x_ += x * m

    x_ = round(x_ / n, 3)
    print('Среднее значение признака:', x_)

    variance = 0
    for x, m in zip(xi, mi):
        variance += (x - x_) ** 2 * m / n

    variance = round(variance, 3)
    print('Дисперсия:', variance)
    S = round(variance ** 0.5, 3)
    print('Среднее квадратичной отклонение:', S)

    v = S / x_
    print('Коэффициент вариации:', v * 100)

    M0 = 0
    M0_count = 0

    for salary in xi:
        if M0_count < salaries.count(salary):
            M0 = salary
            M0_count = salaries.count(salary)

    As = (x_ - M0) / S
    print('Коэффициент ассиметрии:', As)

    u4 = 0
    for x, m in zip(xi, mi):
        u4 += (x - x_) ** 4 * m

    u4 /= n
    print('u4:', u4)
    Ex = (u4 / (S ** 4)) - 3
    print('Эксцесс', Ex)
    return x_, S


xi = sorted(set(salaries))
mi = []
for salary in xi:
    mi.append(salaries.count(salary))
func1(xi, mi)

# часть 3
print()
xi = []
mi = []
d = 10
for sal in range(30, 170, d):
    key = sal + d // 2
    val = len(list(filter(lambda x: sal <= x < sal + d, salaries)))
    xi.append(key)
    mi.append(val)

x_, S = func1(xi, mi)

ti = []
for x in xi:
    ti.append((x - x_) / S)

fmi = []
for t in ti:
    ft = (1 / ((2 * math.pi) ** 0.5)) * math.e ** -((t ** 2) / 2)
    fm = int(ft * n * d / S)
    fmi.append(fm)

print('x_i'.ljust(20), "f_t")
for x, m in zip(xi, fmi):
    print(f'{x}'.ljust(20), m)

plt.bar(xi, fmi, d * 0.7)
plt.yticks(size=20)
plt.xticks(rotation=90, size=20)
plt.savefig("./img2.png")
plt.show()

Fi = [mi[0]]
for m in mi[1:]:
    Fi.append(m + Fi[-1])

Fm = [fmi[0]]
for m in fmi[1:]:
    Fm.append(m + Fm[-1])

Di = []
for i, m in zip(Fi, Fm):
    Di.append(abs(i - m))

D_max = max(Di)
print('Dmax:', D_max)
lamda = D_max / (n ** 0.5)
print('λ:', lamda)
