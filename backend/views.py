from backend import app
from flask_restful import Api, Resource, reqparse, abort
from flask import send_from_directory, jsonify
from flask_cors import CORS, cross_origin

import firebase_admin
from firebase_admin import credentials

firebase_admin.initialize_app()

api = Api(app)

# users = {1: {"name": "nick"}}
users = [
{
  "fullname": "John Doe",
  "email": "johndoe@abc.com",
  "parish": "True",
  "phone": "0712876545"
},
{
  "fullname": "Jane Doe",
  "email": "janedoe@abc.com",
  "parish": "False",
  "phone": "0717672345"
},
{
  "fullname": "Alice Doe",
  "email": "alicedoe@abc.com",
  "parish": "False",
  "phone": "0712987345"
},
{
  "fullname": "Bob Doe",
  "email": "bobdoe@abc.com",
  "parish": "True",
  "phone": "0712123445"
}
]

# @app.route('/users', methods = ["GET", "POST"])
class Userlist(Resource):
    def get(self):
        response = users
        return response, 200
    # def post(self):

class Userlistput(Resource):
    def put(self, name):
        return names.append(name), 201

class Emailtest(Resource):
    def get(self):
        response = users
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
class Emailtestput(Resource):
    def put(self, email):
        console.log(email)
        return emails.append(email), 201

api.add_resource(Userlist, "/users")
api.add_resource(Userlistput, "/users/<string:name>")

api.add_resource(Emailtest, "/emails")
api.add_resource(Emailtestput, "/emails/<string:email>")
