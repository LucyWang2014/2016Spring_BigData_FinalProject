import os
import matplotlib.pyplot as plt

# Load location ID csv
fl = open('../locID.csv')
loc_id = {}
while True:
    line = fl.readline()
    if len(line) == 0:
        break
    line_s = line.split(',')
    num_id = int(line_s[0])
    if line_s[1] not in loc_id.keys():
        loc_id[line_s[1]] = [num_id]
    else:
        loc_id[line_s[1]].append(num_id)

loc_id_reverse = {}
for k, v in loc_id.iteritems():
    for elem in v:
        loc_id_reverse[elem] = k


# Get all information from parts
parts = os.popen('cat ./part*').read()
parts = parts.split('\n')
boro_aggr = {}

for line in parts:
    if len(line) == 0:
        continue
    line_s = line.split(',')
    boro_name = loc_id_reverse.get(int(line_s[0]), 'Unknown')
    if boro_name not in boro_aggr.keys():
        boro_aggr[boro_name] = {'r': 0, 't': 0}
    boro_aggr.get(boro_name)['r'] += float(line_s[1])
    boro_aggr.get(boro_name)['t'] += float(line_s[2])

for k in boro_aggr.keys():
    boro_aggr.get(k)['ratio'] = boro_aggr.get(k).get('t') /\
        boro_aggr.get(k).get('r')

# Pie chart
filter_boro_list = ['Manhattan', 'Queens', 'Brooklyn']
boro_names = boro_aggr.keys()
others_revenue = 0
for n in boro_names:
    if n not in filter_boro_list:
        others_revenue += boro_aggr.get(n).get('r')
boro_names = filter(lambda x: x in filter_boro_list, boro_names)
boro_revenues = [boro_aggr.get(x).get('r') for x in boro_names]
boro_names.append('Others')
boro_revenues.append(others_revenue)

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.15, 0, 0, 0)  # explode 1st slice
plt.pie(boro_revenues, explode=explode, labels=boro_names, shadow=True,
        colors=colors, autopct='%1.1f%%', startangle=140)
plt.savefig('pie.png')

# Ratio
for k, v in boro_aggr.iteritems():
    print(k, '{:.2f}%'.format(v.get('ratio')*100/9.73*15.7))
