import sys
stack = []   

N = int(input())

for i in range(N):

    order = sys.stdin.readline().strip()
    
    if order.find("push") != -1:
        num = int(order.replace("push ",""))
        stack.append(num)

    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
             
    elif order == "size":
        print(len(stack))
        
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

