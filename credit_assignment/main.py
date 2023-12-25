import csv
import config

from lab_1.task_2 import interval_variation_series

with open('ds_salaries.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    salaries = []
    for row in reader:
        salaries.append(int(row['salary_in_usd']))
    print(salaries.sort())
    interval_variation_series(salaries, 30000)

