from random import *
# from eval import calc
import eval
x = randint(1,10)
y = randint(1,10)
ops = ["+","-","*","/"]
op = choice(ops)

errors = [-1,0,0,0,0,0,0,0,1]
error = choice(errors)
# res = 0
# if op == "+" :
#     res = x + y
# elif op == "-" :
#     res = x - y
# elif op == "*" :
#     res = x*y
# else:
#     res = x/y
res = eval.calc(x,y,op)

display_res = res + error
print("{0} {1} {2} = {3}".format(x,op,y,display_res))
answer = input("y/n? ").upper()
# if (error == 0 and answer == "y") or (error != 0 and answer == "n" ) :
    # print("yay")
# else:
    # print("You are wrong ")
if error == 0:  
    if answer == "Y" :
        print("Yay")
    else:
        print("You are wrong")
else:
    if answer == "Y":
        print("you are wrong")
    else :
        print("Yay")

