t1 = list(map(int,input().strip().split(":")))
t2 = list(map(int,input().strip().split(":")))

carry=0

output = []
if t1!=t2:
	for i in range(2,-1,-1):
		if t1[i] > t2[i]+carry:
			if i!=0:
				output.append(t2[i]-t1[i]+60+carry)
				carry = -1
			else:
				output.append(t2[i]-t1[i]+24+carry)
		else:
			output.append(t2[i]-t1[i]+carry)
			carry=0
	output=output[::-1]
	output= ['0'*(2-len(str(i)))+str(i) for i in output]
	print(':'.join(output))
else:
	print("24:00:00")
