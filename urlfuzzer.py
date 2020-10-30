import requests
import sys

banner = """

U   U RRRR  L    FFFF                      
U   U R   R L    F                         
U   U RRRR  L    FFF  u  u zz  zz  eee rrr 
U   U R R   L    F    u  u  z   z  e e r   
 UUU  R  RR LLLL F     uuu  zz  zz ee  r   
                                           
                                           
"""

def fuzzing(host, files):
	try:
		f = open(files, "r", encoding="utf-8")

		for i in f:
			scan = host+i
			scan = scan.rstrip()
			scan += "/"
			
			# send requests to test resposne
			r = requests.get(scan)
			if r.status_code == 200:
				print("Found 200 ", scan)
			elif r.status_code == 403:
				print("Forbidden 403 ", scan)
			else:
				pass
	except KeyboardInterrupt:
			print("Exit")

class main():
	print(banner)
	if len(sys.argv) != 3:
		print("Usage : ", sys.argv[0], " <web target> <directory list>")
		sys.exit()
	else:
		fuzzing(sys.argv[1], sys.argv[2])
