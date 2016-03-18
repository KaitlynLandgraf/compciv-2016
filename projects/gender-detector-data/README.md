# Gender analysis of New York City Payroll information for the office of the mayor
## Preliminary findings

There are more women than men overall, and in every individual salary bracket,
although women's lead on men shrinks in the top two salary brackets compared with the bottom two.
Nobody in the mayor's office makes $250K or above.

#fetch_gender_data.py

Downloads the latest batch of baby name data from the Social Security Administration and dumps it into the tempdata/babynames folder

#wrangle_gender_data.py

Reads a few files from tempdata/babynames and creates a new data file in babynames/wrangledbabynames.json, which is used by gender.detect_gender() to classify the gender of a name.

#fetch_payroll_data.py

downloads all payroll information from the City of New York's public data portal

#wrangle_payroll_data

Since the above file is huge and unweildy, this script wrangles it down to just those people who work in the office of the mayor--almost 700 of them.

#gender.py

This script goes through each employee's first name guessing whether they are male or female

#classify.py

Reads through the wrangled NYC data for the office of the mayor and appends new columns to the file

#analyze.py

Breaks down the number of female and male employees in each salary bracket in the mayor's office.