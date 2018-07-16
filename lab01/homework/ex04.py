# count
from pymongo import MongoClient
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)
db = client.get_default_database()
customers = db['customers']
ads = db.customers.count({'ref' : 'ads'})
events = db.customers.count({'ref' :'events'})
wom = db.customers.count({'ref' :'wom'})
print('ads = ',ads,'\nevents = ',events,'\nwom = ',wom)
# draw a pie chart
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot
# 1 prepare data
labels = ['ads','events','wom']
values = [ads,events,wom]
colors = ['green','red','orange']
explode = [0,0, 0.2]
# 2. plot
pyplot.pie(values,labels = labels,colors = colors,explode = explode)
pyplot.axis('equal')
# 3.show
pyplot.show()