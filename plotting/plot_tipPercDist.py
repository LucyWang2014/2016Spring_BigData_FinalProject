import os
import matplotlib.pyplot as plt

# Get all information from parts
parts = os.popen('cat ./part*').read()
parts = parts.split('\n')
aggr = {}

for line in parts:
    if len(line) == 0:
        continue
    line_s = line.split(',')
    aggr[int(line_s[0])] = int(line_s[1])


# Pie chart
per, number = aggr.keys(), aggr.values()
per = map(lambda x: '{}%'.format(x), per)
per[per.index('100%')] = 'Others'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
plt.pie(number, labels=per, colors=colors, shadow=True, autopct='%1.1f%%', startangle=140)
plt.savefig('pie.png')
