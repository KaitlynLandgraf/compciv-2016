from os.path import join
import operator
dir = '0013-sorted-names/tempdata'
bnames = join(dir, "ssa-babynames-nationwide-2014.txt")

unordered = []
namesdict = {}

group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0

with open(bnames) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if namesdict.get(name):
			namesdict[name] += int(babies)
		else:
			namesdict[name] = int(babies)
i = 1

for name in namesdict:
		unordered.append([name, namesdict[name]])

ordered = sorted(unordered, key=operator.itemgetter(1), reverse=True)

for a in range(len(ordered)):
	if a <= 9:
		group1 += ordered[a][1]
	elif a <= 99:
		group2 += ordered[a][1]
	elif a <= 999:
		group3 += ordered[a][1]
	elif a <= 9999:
		group4 += ordered[a][1]
	else:	
		group5 += ordered[a][1]
i = 1

total_groups = (group1 + group2 + group3 + group4 + group5)

print ('Names 1 to 10:', (round((group1/total_groups)*100,1)))
print ('Names 11 to 100:', (round((group2/total_groups)*100,1)))
print ('Names 101 to 1000:', (round((group3/total_groups)*100,1)))
print ('Names 1001 to 10000:', (round((group4/total_groups)*100,1)))
print ('Names 10001 to',len(ordered),':', (round((group5/total_groups)*100,1)))

	
# print('')
# for thing in mlist[:5]:
# 	ip = str(i) + '.'
# 	print(i, thing[0], thing[1])
# 	i += 1