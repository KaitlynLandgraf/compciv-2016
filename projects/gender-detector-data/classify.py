from os import makedirs
from os.path import join
from csv import DictReader, DictWriter
from gender import detect_gender
DATA_DIR = 'tempdata'
fname = 'wrangled/wrangledofficemayor.csv'

# let's create a extract_usable_name function:
def extract_usable_name(namestr):
    nameparts = namestr.split(', ', 1)
    for nx in nameparts[-1].split(' '):
        if '.' not in nx:
            return nx  # returns the first thing that has no period
    # if we get to this point...then...just return nothing...
    return ""

full_filename = join(DATA_DIR, fname)
# open the salary data
xf = open(full_filename, 'r')
salary_rows = list(DictReader(xf))
xf.close()

classified_headers = list(salary_rows[0].keys()) + ['gender', 'ratio', 'usable_name']

classified_filename = join(DATA_DIR, fname)
print("About to classify", len(salary_rows), 'rows into the file:', classified_filename)

outfile = open(classified_filename, 'w')
output_csv = DictWriter(outfile, fieldnames=classified_headers)
output_csv.writeheader()




xc = 0
for row in salary_rows:
    xc += 1
    first_name = row['First Name']
    print("On row", xc, first_name)
    # skip rows in which row['Employee Name'] is "Not provided"
    if "Not provided" in first_name:
        pass
    else:
        usablename = extract_usable_name(first_name)
        xresult = detect_gender(usablename)
        row['gender'] = xresult['gender']
        row['ratio'] = xresult['ratio']
        row['usable_name'] = usablename
        row['Base Salary'] = (row['Base Salary'][1:])
        # write to the csv file
        output_csv.writerow(row)

outfile.close()