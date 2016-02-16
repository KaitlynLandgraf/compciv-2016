from os.path import join
dir = '0013-sorted-names/tempdata'
bnames = join(dir, "ssa-babynames-nationwide-2014.txt")

flist = []
mlist = []

with open(bnames) as x:
	for line in x:
			name, sex, babies = line.strip().split(',')
			babies = int(babies)
			if 'X' in name:
				if sex == 'F':
					flist.append((name, babies))
				elif sex == 'M':
					mlist.append((name, babies))
			if 'x' in name:
				if sex == 'F':
					flist.append((name, babies))
				elif sex == 'M':
					mlist.append((name, babies))
i = 1

print('Female')
for thing in flist[:5]:
	ip = str(i) + '.'
	print(i, thing[0], thing[1])
	i += 1

i = 1	
print('Male')
for thing in mlist[:5]:
	ip = str(i) + '.'
	print(i, thing[0], thing[1])
	i += 1