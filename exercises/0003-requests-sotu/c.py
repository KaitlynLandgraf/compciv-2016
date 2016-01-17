import requests
resp = requests.get("//imgs.xkcd.com/comics/sword_in_the_stone.png")
print(resp.url)