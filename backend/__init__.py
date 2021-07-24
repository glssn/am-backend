from flask import Flask, request, send_from_directory
from flask_cors import CORS
# imports from video
# from .commands import create_tables
# from .extensions import db, login_manager
# from .models import User
# from .routes.auth import auth
# from .routes.main import main

from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)

import backend.views
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
