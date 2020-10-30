import requests

host = "https://www.google.com"
f = open("wordlist.txt", "r", encoding="utf-8")

for i in f:
	r = requests.get(host+i)
	if r.status_code == 200:
		print("Found 200 ", host+i)
	else:
		pass