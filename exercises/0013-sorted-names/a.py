import os
import requests
os.makedirs('0013-sorted-names/tempdata', exist_ok = True)


URLA = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'

TXTA = requests.get(URLA)

aname = '0013-sorted-names/tempdata/ssa-babynames-nationwide-2014.txt'
afile = open(aname, 'wb')
afile.write(TXTA.content)
afile.close()

print('there are', len(TXTA.text), 'characters in tempdata/ssa-babynames-nationwide-2014.txt')