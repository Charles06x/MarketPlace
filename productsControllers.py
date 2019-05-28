# from app import db
import pymongo
from pprint import pprint

import dns
import pprint
from bson.json_util import dumps, _json_convert
from bson.objectid import ObjectId

con = pymongo.MongoClient('mongodb+srv://root-condor:root-condor@condormarket-kmpgf.mongodb.net/CondorMarket?retryWrites=true')
db = con.CondorMarket

from flask import Response
from flask_restful import Resource

prods = db.products
img = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Simple_cardboard_box.svg/1280px-Simple_cardboard_box.svg.png"
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

class getAllProducts(Resource):
    def get(self):
        prod = (list(prods.find().sort("productName", pymongo.ASCENDING)))
        firstProd = prod[0]
        for i in range(len(prod)):
            auxP = prod[i]
            auxOi = _json_convert(auxP["_id"])
            auxP["_id"] = auxOi["$oid"]
            prod[i] = auxP
        if prod:            
            data = {}
            data["products"] = prod
            data = dumps(data)
            resp = Response(data, status=200, mimetype='application/json')            
            return resp


class getOneProduct(Resource):
    def get(self, id):
        prod = prods.find_one({'_id': ObjectId(id)})
        print(prod)
        auxP = prod
        auxOi = _json_convert(auxP["_id"])
        auxP["_id"] = auxOi["$oid"]
        prod = auxP
        data = {}
        data["product"] = prod
        return data