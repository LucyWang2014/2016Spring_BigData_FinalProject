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


# Pie chart-1, 0 vs not-0
zeroTip = aggr.get(0)
nonZeroTip = sum(aggr.values()) - zeroTip
colors = ['gold', 'yellowgreen']
explode = (0, 0)  # explode 1st slice
plt.pie([zeroTip, nonZeroTip], explode=explode, labels=['Tip', 'NoTip'], shadow=True,
        colors=colors, autopct='%1.1f%%', startangle=140)
plt.savefig('pie1.png')

# Pie chart-2, $1, $2, $3, $4, $5, $6, others
plt.figure()
tips = [aggr.get(x) for x in range(1, 5)]
rest = nonZeroTip - sum(tips)
tips.append(rest)
labels = ['$1', '$2', '$3', '$4', 'more']
plt.pie(tips, labels=labels, shadow=True, autopct='%1.1f%%', startangle=140)
plt.savefig('pie2.png')
