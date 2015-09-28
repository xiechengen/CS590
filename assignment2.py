import json
import math
import array
import time


def myhash(x,i):
	return hash(x+i)%20000

f = open('tweetstream.txt','r')
N = 100000

##Using the equation we can calculate the t
t = 6 
b = 200000


sample = ['freedom', 'songs']

for s in sample:
	print s
###creat a matix 
matrix = []
for _ in xrange(t):
	table = array.array("l", (0 for _ in xrange(b)))
	matrix.append(table)

start = time.time()

count = 0

for i in range(N):
	print i
	try:
		
		nextTweet = json.loads(f.next())
		tag = nextTweet['entities']['hashtags']
		createTime = nextTweet['created_at']
		
		if tag != []:
			count +=1
			for k in tag:
				for j in range(6):
					matrix[j][myhash(k['text'],str(j))] += 1
		
		
		end = time.time()
		if end - start >= 1:
			start = end
			target = open('a2q1output.txt','a')
			target.write(str(end) +',')

			for s in sample:
				target.write(s + ',')
				hashtagCount = min(matrix[i][myhash(s,str(i))] for i in range(6))
				target.write(str(hashtagCount) + ",")
			target.write("\n")
			target.close()

	except:
		pass


#print count
print min(matrix[i][myhash("instagram",str(i))] for i in range(6))

	