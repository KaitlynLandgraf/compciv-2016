import json
f = open("tempdata/googlemaps/stanford.json", 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

print (mydict['results'][0]['formatted_address'], mydict['results'][0]['geometry']['location']['lng'], mydict['results'][0]['geometry']['location']['lat'], end ='; ')