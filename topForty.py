import os
import operator

csv = open("/home/srishti/blogs.csv","r")#PATH
moods = {}
blog = csv.readline()
i = 0

while(blog != ''):
	blog = blog.split(',')
	if(len(blog) < 2):
		blog = csv.readline()
		continue
	if(len(blog[0]) != 0):
		moods[blog[1]] = moods.get(blog[1],0) + 1
	blog = csv.readline()
	i+= 1
	
x = sorted(moods.items(), key=operator.itemgetter(1), reverse=True)
	
print("Sorted, number of moods = " + str(len(moods)))
topMoods = []
top = {}
iter = {}
for i in range(0,40):
	top[x[i][0]] = x[i][1]
	iter[x[i][0]] = 0
	topMoods.append(x[i][0])

path = "/home/srishti/trainData500/"#PATH WHERE BLOG FILES ARE TO BE SAVED
if not os.path.exists(path):
	os.mkdir(path)
		
csv = open("/home/srishti/blogs.csv","r")#PATH WHERE CSV IS STORED
blog = csv.readline()

while(blog != ''):
	blog = blog.split(',')
	if(len(blog) < 2):
		blog = csv.readline()
		continue
	if(len(blog[0]) != 0):
		moodName = blog[1]
		if top.get(blog[1],0) > 0 and iter[moodName] < 400: #DEFINES A BOUND ON THE NUMBER OF POSTS ASSOCIATED WITH A MOOD
			if not os.path.exists(path + moodName[:(len(moodName) - 1)] + "/"):
				os.mkdir(path + moodName[:(len(moodName) - 1)] + "/")
			f = open(path + moodName[:(len(moodName) - 1)] + "/" + str(iter[blog[1]]) + ".txt", "w")
			iter[moodName] += 1
			f.write(blog[0])
	blog = csv.readline()
	
for i in topMoods:
	print(str(top[i]) + " blogs found for mood " + i)

for i in topMoods:
	print "\"" + i[:(len(i) - 1)] + "\",",#PRINT TO ALLOW COPYING INTO "CLASSES" FIELD OF CLASSIFY
