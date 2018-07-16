from pymongo import MongoClient
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client = MongoClient(uri)
db = client.get_default_database()
posts = db ['posts']
jokes = {"title" : "Con vẹt phát điên",
"author" : "Liên",
"content" : """Boss cảnh cáo học sinh:
-Không bao giờ được hôn động vật,sẽ bị lây các bệnh khác nhau.Ai có thể đưa ra ví dụ?
-Em ạ - Crazy đứng dậy - Cô em luôn hôn con vẹt của mình
- Thì sao???...
- Con vẹt phát điên
<copy có chỉnh sửa...>""" }
posts.insert_one(jokes)

