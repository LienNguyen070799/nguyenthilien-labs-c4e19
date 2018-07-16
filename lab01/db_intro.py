# database
# pymongo
from pymongo import MongoClient
uri ="mongodb://admin:admin123@ds135421.mlab.com:35421/c4e_19_labs"
# 1. connect database
client = MongoClient(uri)

# 2. get database
db = client.get_default_database()

# 3. create collection
games = db['games']
# # 4.create document
# cac_loai_hoa_qua = {
#     "cam" : "mau cam",
#     "dua": "xanh let",
#     "chuoi" : "mau vang",
#     " boss" : "hoi trang"
# }
# # 5.insert doc into document
# fruit.insert_one(cac_loai_hoa_qua)


# get all documents
all_games = games.find()

print(all_games[0]['name'])