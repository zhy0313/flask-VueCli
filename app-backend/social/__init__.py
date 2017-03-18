import uuid

from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS

__database_name = 'app'

app = Flask(__name__)
#CORS(app=app, resources= r'/api/*')
app.host = '127.0.0.2'
app.secret_key = uuid.uuid1()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev:23579@localhost/{}'.format(__database_name)
database = SQLAlchemy(app=app)
marshmallow = Marshmallow(app=app)

from social.api.v1 import view
from social import model
