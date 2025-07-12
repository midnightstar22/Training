n=int(input())
ins=[""]*n
stack=[]
q=0
k=1

while (q!=n):
    ins[q]=input()
    q+=1

q=0
while (q!=n+1):
    if ins[q].startswith("PUSH"):
        s=ins[q]
        stack.append(int(s[5:]))
        q+=1
    elif ins[q].startswith("STORE"):
        if stack:
            reg=stack[-1]
            stack.pop()
        q+=1
        
    
        
    elif ins[q].startswith("LOAD"):
        stack.append(reg)
        q+=1
    elif ins[q].startswith("PLUS"):
        if stack:
            a=stack[-1]
            stack.pop()
            b=stack[-1]
            stack.pop()
            summ=a+b
            stack.append(summ)
        q+=1
    elif ins[q].startswith("TIMES"):
        if stack:
            a=stack[-1]
            stack.pop()
            b=stack[-1]
            stack.pop()
            mul=a*b
            stack.append(mul)
        q+=1
    elif ins[q].startswith('IFZERO'):
        if stack[-1]!=0:
            stack.pop()
            q+=1
        else:
            stack.pop()
            s=ins[q]
            q=int(s[7:])
    else:

        print(stack[-1])
        break
