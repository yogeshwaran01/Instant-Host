import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Configurations:

    SQLALCHEMY_DATABASE_URI = os.environ.get("SQL_DATABASE_URL")
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir + "/app.db"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_DIR = basedir + "/app/uploads"
    MAX_CONTENT_LENGTH = 1024
