import os
import requests
import json
os.makedirs("tempdata/googlemaps", exist_ok = True)
os.makedirs("tempdata/mapzen", exist_ok = True)


URLA = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
URLB = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'

TXTA = requests.get(URLA)
TXTB = requests.get(URLB)

aname = 'tempdata/googlemaps/stanford.json'
afile = open(aname, 'wb')
afile.write(TXTA.content)
afile.close()

bname = 'tempdata/mapzen/stanford.json'
bfile = open(bname, 'wb')
bfile.write(TXTB.content)
bfile.close()

print('Downloading from:', URLA)
print('Writing to:', aname)
print('Wrote', len(TXTA.text.splitlines()), 'lines and', len(TXTA.text), 'characters')
print('Downloading from:', URLB)
print('Writing to:', bname)
print('Wrote', len(TXTB.text.splitlines()), 'lines and', len(TXTB.text), 'characters')