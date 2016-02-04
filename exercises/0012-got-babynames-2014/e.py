from os.path import join
dir = '0012-got-babynames-2014/tempdata'
f = join(dir, "ssa-babynames-nationwide-2014.txt")

fbabies = mbabies = 0

with open(f) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			fbabies += int(line.split(',')[2])
		if sex == 'M':
			mbabies += int(line.split(',')[2])

print('F:', fbabies)
print('M:', mbabies)