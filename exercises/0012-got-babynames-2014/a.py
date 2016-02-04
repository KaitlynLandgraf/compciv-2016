import os
import requests
os.makedirs('0012-got-babynames-2014/tempdata', exist_ok = True)


URLA = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'

TXTA = requests.get(URLA)

aname = '0012-got-babynames-2014/tempdata/ssa-babynames-nationwide-2014.txt'
afile = open(aname, 'wb')
afile.write(TXTA.content)
afile.close()

print('there are', len(TXTA.text.splitlines()), 'in tempdata/ssa-babynames-nationwide-2014.txt')
