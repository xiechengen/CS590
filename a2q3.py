import json
import math
import array
import gmpy

f = open('tweetstream.txt','r')

#length = 10000000
#bitmap = array.array('l', (0 for _ in range(length)))

def myhash(x):
	return hash(x)%100000000000

max = 0

for i in range(100000):
	try:
		
		nextTweet = json.loads(f.next())
		tag = nextTweet['entities']['hashtags']
		if tag != []:
			for t in tag:
				#Compute k(x) = Tail0(h(x))
				k = gmpy.scan1(myhash(t['text']))
				
				if k > max:
					max = k	
				
				print i, ",", 2**max

	except:
		pass

		
		

