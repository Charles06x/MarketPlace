from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

import pymongo
import dns
import pprint

from productsControllers import *

app = Flask(__name__)
con = pymongo.MongoClient('mongodb+srv://root-condor:root-condor@condormarket-kmpgf.mongodb.net/CondorMarket?retryWrites=true')
db = con.CondorMarket
CORS(app)
api = Api(app)
api.add_resource(getAllProducts, '/api/products')
api.add_resource(getOneProduct, '/api/products/<id>')
api.add_resource(getCategories, '/api/categories')
api.add_resource(getProductsByCategory, '/api/<productCategory>/products')

if __name__ == '__main__':
    app.run(debug=True)