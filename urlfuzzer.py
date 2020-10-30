import requests
import sys

def fuzzing(files, host):
	f = open(files, "r", encoding="utf-8")

	for i in f:
		r = requests.get(host+i)
		if r.status_code == 200:
			print("Found 200 ", host+i)
		else:
			pass

class main():
	if len(sys.argv) != 3:
		print("Usage : ", sys.argv[0], " <web target> <directory list>")
		sys.exit()
	else:
		fuzzing(sys.argv[1], sys.argv[2])
