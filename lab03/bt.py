x = int(input("x = "))
operation = input ("operation(+,-,*,/): ")
y = int(input("y = ")) 
print("*"*30)
res = 0
if operation == "+" :
    # print(x,"+",y,"=",x+y)
    res = x+y
elif operation == "-" :
    res = x-y
elif operation=="*" :
    res = x*y
else:
    res = x/y
print("{0} {1} {2}= {3}".format(x,operation,y,res))
print("*"*30)
