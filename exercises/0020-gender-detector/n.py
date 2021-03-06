from os.path import join
from zoofoo import detect_gender
import csv
DATA_DIR = 'tempdata'
WRANGLED_FINAL_FILENAME = join(DATA_DIR, 'wrangledbabynames.json')
NAMES_DATA_ROWS = list(csv.DictReader(open(WRANGLED_FINAL_FILENAME)))

NAMES_TO_TEST = ['Michael', 'Kelly', 'Kanye', 'THOR', 'casey', 'Arya', 'ZZZblahblah']

namecount = {'M': 0, 'F': 0, 'NA': 0}
babycount = {'males': 0, 'females': 0}
for name in NAMES_TO_TEST:
    result = detect_gender(name)
    print(name, result['gender'], result['ratio'])
    if result['gender']:
        namecount[result['gender']] += 1

    if result['gender'] != 'NA': 
        babycount['males'] += result['males']
        babycount['females'] += result['females']

print("Total:")
print("F:", namecount['F'], 'M:', namecount['M'], 'NA:', namecount['NA'])
print('females:', babycount['females'], 'males:', babycount['males'])