from app import db
from pprint import pprint
prods = db.products
pprint(list(prods.find()))
img = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Simple_cardboard_box.svg/1280px-Simple_cardboard_box.svg.png"
#p = Products(productName="test", productPrice=50, productCategory="Computers", productSeller="Me", productDescription="NONE", productQuantity=20, productImg=img)
# p = {
#     "productName": "pythontest",
#     "productPrice": 50,
#     "productCategory": "testing python",
#     "productSeller": "Me",
#     "productDescription": "None",
#     "productQuantity": 20,
#     "productImg": img
# }

# print(prods.insert_one(p).inserted_id)

#
# class getProducts(Resource):
#     def get(self):
#         lst = []
#         prods =
