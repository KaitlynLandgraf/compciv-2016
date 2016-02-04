from os.path import join
dir = '0012-got-babynames-2014/tempdata'
bnames = join(dir, "ssa-babynames-nationwide-2014.txt")

game = thrones = 0

with open(bnames) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		if name == 'Daenerys':
			thrones += int(babies)
		elif 'Khalees' in name or 'Khaless' in name:
			game += int(babies)
print ('Daenerys:', thrones)
print ('Khaleesi:', game)