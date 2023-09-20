for i in range(int(input())):
    stack = []
    boolean= "YES"
    
    for j in input():
        if j == '(':
            stack.append(j)
        elif len(stack) >0:
            stack.pop()
            
        else:
            boolean = "NO"
    if len(stack) >0:
        boolean = "NO"
        
    print(boolean)