#!/usr/bin/python3
import os
import sys
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from pymongo import MongoClient
from json import dumps
from dotenv import load_dotenv
#from flask_jwt_extended import JWTManager
from flask_cors import CORS


load_dotenv()

from controllers.domain import Domain


app = Flask(__name__)
#app.config['SECRET_KEY'] = os.getenv("APP_SECRET")
#app.config['JWT_SECRET_KEY'] = os.getenv("APP_SECRET")

#app.mongo = MongoClient(os.getenv("MONGO_URL"))
api = Api(app, prefix="/api/v1")
##
api.add_resource(Domain, '/domain/get')




#jwt
#jwt = JWTManager(app)

#Cors
cors = CORS(app, resources={r"/api/*": {"origins": os.getenv("ORIGIN_URL") }})

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))