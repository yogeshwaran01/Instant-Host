from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_compress import Compress
from flask_cors import CORS

from .configurations import Configurations

app = Flask(__name__)
app.config.from_object(Configurations)

CORS(app)
Compress(app)

database = SQLAlchemy(app)

migrate = Migrate(app, database)

from .models import SourceCode
from .views import *
