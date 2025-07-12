l1=list(map(int,input().split()))
n=l1[0]
d=l1[1]

w=list(map(int,input().split()))
       
w.sort(reverse=True)

       

total=0
for k in range(d):
       total+=w[k]
print(total)
       
