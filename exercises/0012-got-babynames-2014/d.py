from os.path import join
dir = '0012-got-babynames-2014/tempdata'
bnames = join(dir, "ssa-babynames-nationwide-2014.txt")

flist = []
mlist = []

with open(bnames) as x:
	for line in x:
			name, sex, babies = line.strip().split(',')
			babies = int(babies)
			if sex == 'F':
				flist.append((name, babies))
			if sex == 'M':
				mlist.append((name, babies))
i = 1

print('top baby girl names')
for thing in flist[:5]:
	ip = str(i) + '.'
	print(i, thing[0], thing[1])
	i += 1

i = 1	
print('top baby boy names')
for thing in mlist[:5]:
	ip = str(i) + '.'
	print(i, thing[0], thing[1])
	i += 1






# game = thrones = 0




# # with open(bnames) as x:
# 	for line in x:
# 		sorted(name, sex, babies) = line.strip().split(',')
# 		if sex == 'F':
# 			thrones += (str(name), int(babies))
# 		elif sex == 'M':
# 			game += (str(name), int(babies))
# print (name, thrones)(5)
# print (name, game)(5)