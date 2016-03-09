from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'

for fname in glob(join(DATA_DIR, '*.txt')):
  tally = {'M': set(), 'F': set()}
  year = basename(fname)[3:7]
  if year >= "1950":
    for line in open(fname, 'r'):
        name, gender, babies = line.split(',')
        tally[gender].add(name)
    print(year)
    print("F:", str(len(tally['F'])).rjust(6), "M:", str(len(tally['M'])).rjust(6))
    print("F/M baby ratio: ", round(100 * (len(tally['F'])) / (len(tally['M']))))