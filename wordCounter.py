import os

bcount=0
filename = input('Enter a file name: ')
if(not os.path.isfile(filename)):
	print("File doesn't exists")
else:
	f=open(filename,'r')
	content=f.read()
	lcount=len(content.split("\n"))
	print(lcount)
	wcount=len(content.split(" "))
	print(wcount)
	for words in content.split(" "):
		bcount=bcount+len(words)
	print(bcount)
	f.close()

