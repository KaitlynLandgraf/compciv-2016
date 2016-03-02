import requests
from os.path import join, basename
from os import makedirs
from glob import glob
import json
API_ENDPOINT = 'https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify'
PICS_DIR = 'pics'
RECOG_DIR = 'responses'
makedirs(RECOG_DIR, exist_ok=True)

DEFAULT_PARAMS = {
    'version': '2015-12-02'
}
DEFAULT_HEADERS = {
    'Accept': 'application/json'
}

creds = json.load(open("creds_watson_visual.json"))
my_username = creds['credentials']['username']
my_password = creds['credentials']['password']
myauth = (my_username, my_password)

for fname in glob(join(PICS_DIR, '*.jpg')):
    print("Testing", fname)

    with open(fname, 'rb') as imgdata:
        mydict = {}
        mydict['images_file'] = (fname, imgdata)
        resp = requests.post(API_ENDPOINT, params=DEFAULT_PARAMS,
                        auth=myauth, headers=DEFAULT_HEADERS,
                        files=mydict)
    print(resp.status_code)

    if resp.status_code == 200:
        oname = join(RECOG_DIR, basename(fname + '.json'))
        print("Writing to:", oname)

        with open(oname, 'w') as o:
            o.write(resp.text)

    else:
        print("Error code was", resp.status_code, " -- not: 200")