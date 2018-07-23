
def is_inside(p,re) :
    if re[0] <= p[0] <= (re[0]+ re[2]) and re[1] <= p[1] <= (re[1] + re[3]) :
        # p[0],p[1] là tọa độ x,y của điểm
        # re[0],re[1] là tọa độ bắt đầu hình chữ nhật
        # re[3],re[4] lần lượt là chiều rộng và chiều dài của hình chữ nhật
        print(True)
    else :
        print(False)
is_inside([100,200],[60,140,50,100])
