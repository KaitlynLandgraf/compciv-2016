import requests
from os import makedirs
from os.path import basename, join
DATA_DIR = 'tempdata'
makedirs(DATA_DIR, exist_ok=True)
SOURCE_DATA_URL = 'https://data.cityofnewyork.us/api/views/48jx-usvd/rows.csv?accessType=DOWNLOAD'
 
print("Downloading", SOURCE_DATA_URL)
resp = requests.get(SOURCE_DATA_URL)
data_file_path = join(DATA_DIR, basename(SOURCE_DATA_URL))

with open(data_file_path, 'w') as f:
    f.write(resp.text)
    print("Wrote", len(resp.text), "to", data_file_path)