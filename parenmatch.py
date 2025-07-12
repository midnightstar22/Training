s = input()
stack = []
flag = 1  

for i in s:
    if i == "{":
        stack.append(i)
    elif i == "}":
        if not stack:
            flag = 0  
            break
        stack.pop()

if flag == 1 and not stack:
    print("Matching")
else:
    print("Not Matching")
