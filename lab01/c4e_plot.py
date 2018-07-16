import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

# 1.prepare data
labels = ["iOs", "android","Web"," React Native"]
values = [15,15,40,30] 
# (values ko nhat thiet co tong = 100)
colors = ["green", "red","blue","gold"]
explode = [0,0,0,0.2]
# 2. plot
pyplot.pie(values, labels = labels,colors = colors, explode = explode)
pyplot.axis("equal")

# 3. show
pyplot.show()


# xem cac do thi khac di.:3