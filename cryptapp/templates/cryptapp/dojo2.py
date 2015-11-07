f1 = '/home/dc-10/Downloads/IRC\ logs/1'
f2 = '/home/dc-10/Downloads/IRC\ logs/2.txt'
f3 = '/home/dc-10/Downloads/IRC\ logs/3.txt'
f4 = '/home/dc-10/Downloads/IRC\ logs/4.txt'

files = [f1,f2,f3,f4]
w= raw_input()
r= raw_input()
 
count = 0
for f in files:

	with open(f,'r') as f:
	    for line in f:
	        count += line.count(w)
	        line.replace(w, r)

if count==0:
	print "error word not found!!"	        
