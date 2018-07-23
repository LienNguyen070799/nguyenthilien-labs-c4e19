# dinh nghia, 
# funtion argumets (tham so dau vao )
def calc(x, y, op):
    res = 0
    if op == "+" :
        res = x + y
    elif op == "-" :
        res = x - y
    elif op == "*" :
        res = x*y
    else:
        res = x/y
    return res 
    # khi goi lenh return thi se dung moi lenh nam duoi(giong break)
# lay ra
# result = calc(3, 7, "+")
# print(result)
# function la dong tu