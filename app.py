from flask import Flask, request
from flask_restful import Resource, Api

import pymongo
import dns
import pprint

app = Flask(__name__)
con = pymongo.MongoClient('mongodb+srv://root-condor:root-condor@condormarket-kmpgf.mongodb.net/CondorMarket?retryWrites=true')
db = con.CondorMarket

api = Api(app)