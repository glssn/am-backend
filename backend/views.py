from backend import app
from flask_restful import Api, Resource, reqparse, abort
from flask import send_from_directory, jsonify
from flask_cors import CORS, cross_origin

api = Api(app)

user_put_args = reqparse.RequestParser()
user_put_args.add_argument("name", type=str, help="User name must be specified", required=True)

users = {1: {"name": "nick"}}
names = ['nick', 'james']
emails = ['a@b.c', 'me@you.me']

def abort_if_no_user(user_id):
    if user_id not in users:
        abort(404, message="user not found")

def abort_if_user_exist(user_id):
    if user_id in users:
        abort(409, message="user with id \"" + str(user_id) + "\" already exists")


# @app.route("/")
# def hello():
#     return "Hello world!"

class HelloApiHandler(Resource):
  def get(self):
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello Nick"
      }

  def post(self):
    print(self)
    parser = reqparse.RequestParser()
    parser.add_argument('type', type=str)
    parser.add_argument('message', type=str)

    args = parser.parse_args()

    print(args)
    # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

    request_type = args['type']
    request_json = args['message']
    # ret_status, ret_msg = ReturnData(request_type, request_json)
    # currently just returning the req straight
    ret_status = request_type
    ret_msg = request_json

    if ret_msg:
      message = "Your Message Requested: {}".format(ret_msg)
    else:
      message = "No Msg"

    final_ret = {"status": "Success", "message": message}

    return final_ret

api.add_resource(HelloApiHandler, '/api')

class User(Resource):
    def get(self, user_id):
        abort_if_no_user(user_id)
        return users[user_id] # return information about that user

    def put(self, user_id):
        abort_if_user_exist(user_id)
        args = user_put_args.parse_args()
        users[user_id] = args
        return users[user_id], 201 # successfully added user with information

    def delete(self, user_id):
        abort_if_no_user(user_id)
        del users[user_id]
        return 'user deleted', 204

class Userlist(Resource):
    def get(self):
        response = names
        return response, 200

class Userlistput(Resource):
    def put(self, name):
        return names.append(name), 201

class Emailtest(Resource):
    def get(self):
        response = emails
        # response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
class Emailtestput(Resource):
    def put(self, email):
        console.log(email)
        return emails.append(email), 201

api.add_resource(User, "/user/<int:user_id>")
api.add_resource(Userlist, "/users")
api.add_resource(Userlistput, "/users/<string:name>")

api.add_resource(Emailtest, "/emails")
api.add_resource(Emailtestput, "/emails/<string:email>")
