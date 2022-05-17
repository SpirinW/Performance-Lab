import sys
nums = [int(i) for i in [str(s) for s in open(sys.argv[1], 'r')]]
avg, diff, key= sum(nums)/len(nums), float(abs(max(nums))), -1
for i in nums:
	if abs(i - avg) < abs(diff):
		diff = i - avg
		key = i
c = 0
for i in nums:
	if i < key:
		while(i < key):
			i+=1
			c+=1
	elif i > key:
		while(i > key):
			i-=1
			c+=1
print(c)