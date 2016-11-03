import os
import operator

csv = open("/home/srishti/blogs.csv","r")
pos =["amused", "happy", "cheerful", "accomplished", "content", "excited", "awake", "calm", "bouncy", "chipper", "ecstatic",  "creative", "hopeful", "good", "thoughtful", "loved", "contemplative", "blah", "sleepy", "okay"]
neg=["tired", "bored", "annoyed", "confused", "busy", "sick", "anxious", "exhausted", "crazy", "depressed", "curious", "drained", "sad", "aggravated", "blank", "hungry", "cold", "pissed off", "frustrated", "cranky"]
path="/home/srishti/biclassification/"
pospath = path + "pos/"
negpath = path + "neg/"
poscount = 0
negcount = 0

if not os.path.exists(path):
	os.mkdir(path)
if not os.path.exists(pospath):
	os.mkdir(pospath)
if not os.path.exists(negpath):
	os.mkdir(negpath)
blog = csv.readline()

while(blog != ''):
	blog = blog.split(',')
	if(len(blog) < 2):
		blog = csv.readline()
		continue
	if(len(blog[0]) != 0):
		moodName = blog[1][:(len(blog[1]) - 1)]
		if moodName in pos and poscount < 50000:
			f = open(pospath + str(poscount) + ".txt", "w")
			poscount += 1
			f.write(blog[0])
		if moodName in neg and negcount < 50000:
			f = open(negpath + str(negcount) + ".txt", "w")
			negcount += 1
			f.write(blog[0])
	blog = csv.readline()

print "neg=" + str(negcount) + " pos=" + str(poscount)
