import json
f = open("tempdata/mapzen/stanford.json", 'r')
txt = f.read()
f.close()

mydict = json.loads(txt)

for x in range(len(mydict['features'])):
	print (mydict['features'][x]['properties']['label'], end =';')
	print (mydict['features'][x]['properties']['confidence'], end ='; ')
	print (mydict['features'][x]['geometry']['coordinates'][0], end ='; ')
	print (mydict['features'][x]['geometry']['coordinates'][1])