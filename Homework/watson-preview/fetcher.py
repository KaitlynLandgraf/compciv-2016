import requests
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)
destination = ('a', 'b', 'c', 'd', 'e')
i = 0

URLS =	["http://images.nypl.org/index.php?id=swope_624578&t=w", "http://images.nypl.org/index.php?id=815025&t=w", "http://images.nypl.org/index.php?id=TH-00775&t=w", "http://images.nypl.org/index.php?id=1947075&t=w", "http://images.nypl.org/index.php?id=1227905&t=w"]

for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = 'pics/'+destination[i]+'.jpg'
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)
    i += 1