

n = int(input())
day = list(map(int, input().split()))
night = list(map(int, input().split()))
time = int(input())
night1 = []
day.sort()
index=0
for i in range(n):
   
        if day[i]==night[i]:
           continue
        
        else:
            index=i

# if index!=0:
#     night1=night[:index]
#     night1.sort(reverse=True)
#     night[:index]=night1
night.sort(reverse=True)
cost=0
for i in range(n):
    total=day[i]+night[i]
    if total>time:
        cost+=(total-time)*100

print(cost)


    
        
    
