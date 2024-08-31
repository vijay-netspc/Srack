n=int(input())
string=[]
for i in range(n):
	count_in=0
	temp=input().strip()
	for s in temp:
		if(s.islower()):
			count_in+=1
	string.append((temp,count_in,i))
for i in range(n):
	min_ind=i
	for j in range(i+1,n):
		if string[j][1]<string[min_ind][1] or (string[j][1]==string[min_ind][1] and string[j][2]<string[min_ind][2]):
			min_ind=j
	string[min_ind],string[i]=string[i],string[min_ind]
	print(string[i][0])
