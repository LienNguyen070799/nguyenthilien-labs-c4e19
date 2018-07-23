from random import *

def generate_quiz():
    # Hint: Return [x, y, op,display_result]
    x = randint(1,10)
    y = randint(1,10)
    ops = ["+","-","*","/"]
    op = choice(ops)
    errors = [-1,0,0,1]
    error = choice(errors)
    res = 0
    if op == "+" :
        res = x + y
    elif op == "-" :
        res = x - y
    elif op == "*" :
        res = x*y
    else:
        res = x/y
    display_res = res + error
    return [x, y, op, display_res]

def check_answer(x, y, op, display_res, user_choice):
    if op == "+" :
        res = x + y
    elif op == "-" :
        res = x - y
    elif op == "*" :
        res = x*y
    else:
        res = x/y
    if (display_res == res and user_choice == True) or (display_res != res and user_choice == False ) :
        return True
    else:
        return False
    # user_choice = True/False
    # return True/False
