n,m=map(int,input().split())
A=[]
B=[]



for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)
    


for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

print("First Matrix:")
for row in A:
    print(*row)
print("Second Matrix:")
for row in B:
    print(*row)

print("Sum of the two matrices is:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j] + B[i][j])
    print(*row)

        


        
    
    
    
    
    
        
            
        
        
        
        
        
        
    






        
        
