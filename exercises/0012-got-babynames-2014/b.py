from os.path import join
dir = '0012-got-babynames-2014/tempdata'
f = join(dir, "ssa-babynames-nationwide-2014.txt")

babies = 1

with open(f) as x:
	for line in x:
		babies += int(line.split(',')[2])

print("there are", babies, "babies whose names were recorded in 2014.")