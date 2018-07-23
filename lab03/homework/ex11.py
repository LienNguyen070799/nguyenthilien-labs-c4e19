# x = int(input(""))
# y = int(input(""))
# width = int(input(" Chiều rộng hcn: "))
# height = int(input(" Chiều dài hcn : "))
# x2 = int(input(" Hoành độ điểm bắt đầu hcn : "))
# y2 = int(input(" Tung độ điểm bắt đầu hcn : ")
# diem = [x,y]
# rectangle = [x2,y2,width,height]
def is_inside(p = [x,y],re = [x2,y2,width, height]) :
    if x2 <= x <= (x2+ width) and y2 <= y <= (y2 + height) :
        return True
    else :
        return False
is_inside([100,200],[60,240,50,100])
