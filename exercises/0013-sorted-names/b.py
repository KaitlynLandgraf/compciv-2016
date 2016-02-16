from os.path import join
import operator
from operator import itemgetter, attrgetter
dir = '0013-sorted-names/tempdata'
bnames = join(dir, "ssa-babynames-nationwide-2014.txt")

records_list = []

def sort_table(records_list, cols):
	return sorted(records_list, key=operator.itemgetter(cols), reverse=True)

with open(bnames) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		row = [name, sex, int(babies)]
		records_list.append(row)
i = 1

for thing in sort_table(records_list, 2)[:10]:
	ip = str(i) + '.'
	print(i, thing[0], thing[1], thing[2])
	i += 1