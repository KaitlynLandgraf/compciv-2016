import json
f = open("tempdata/googlemaps/stanford.json", 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

for x in range(len(mydict['results'][0]['address_components'])):
	print (mydict['results'][0]['address_components'][x]['long_name'], end ='; ')