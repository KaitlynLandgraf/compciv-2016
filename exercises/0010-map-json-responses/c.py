import json
f = open("tempdata/googlemaps/stanford.json", 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

if len(mydict['results'][0]['formatted_address']) == 0:
	print ('no value')
elif len(mydict['results'][0]['formatted_address'].splitlines()) == 1:
	print (mydict['results'][0]['formatted_address'])
else:
	print ('multiple results')