from os.path import join
import string
dir = '0012-got-babynames-2014/tempdata'
f = join(dir, "ssa-babynames-nationwide-2014.txt")

mydict = {}

for line in open(f):
    	name, sex, babies = line.strip().split(',')
    	last_letter = name[-1]
    	if mydict.get(last_letter):
        	mydict[last_letter] += int(babies)
    	else:
        	mydict[last_letter] = int(babies)
for last_letter in string.ascii_lowercase:
	val = mydict.get(last_letter)
	ip = last_letter + '.'
	print (ip, val)