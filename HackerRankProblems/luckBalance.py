import sys

test = map(int,raw_input().strip().split(' '))

testcases = test[0]
canLose = test[1]
total = 0
important = []
unimportant = []
overall = []

for i in xrange(testcases):
	readLine = map(int,raw_input().strip().split(' '))
	if readLine[1] == 0:
		unimportant.append(readLine[0])
	else:
		important.append(readLine[0])

important.sort(reverse=True)

for i in unimportant:
	total = total + i

for i in xrange(len(important)):
	if i < canLose:
		total = total + important[i]
	else:
		total = total - important[i]
print total




