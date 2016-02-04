from os.path import join
import string
dir = '0012-got-babynames-2014/tempdata'
f = join(dir, "ssa-babynames-nationwide-2014.txt")

m_dict = {}
f_dict = {}

for line in open(f):
    	name, sex, babies = line.strip().split(',')
    	last_letter = name[-1]
    	if sex == 'F':
    		if f_dict.get(last_letter):
        		f_dict[last_letter] += int(babies)
    		else:
        		f_dict[last_letter] = int(babies)
    	if sex == 'M':
    		if m_dict.get(last_letter):
        		m_dict[last_letter] += int(babies)
    		else:
        		m_dict[last_letter] = int(babies)
print ((('letter').ljust(8)),(('F').rjust(8)),(('M').rjust(8)))
print('--------------------------')
for last_letter in string.ascii_lowercase:
	fval = f_dict.get(last_letter)
	mval = m_dict.get(last_letter)
	ip = last_letter
	print ((str(ip).ljust(8)),(str(fval).rjust(8)),(str(mval).rjust(8)))