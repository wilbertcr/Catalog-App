import json
from os import path

def build_db_uri(options):
    # SQLAlchemy's format is:
    # dialect+driver://username:password@host:port/database
    return options['dialect'] + "://" + \
           options['driver'] + \
           options['username'] + ":" + \
           options['password'] + "@" + \
           options['host'] + ":" + \
           options['port'] + "/" + \
           options['dbname']


# Statement for enabling the development environment
DEBUG = True

# Define the application top level directory
BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

# Define the database - we are working with
# SQLite for this example
DB_CONNECT_OPTIONS = {'dialect': "postgresql",
                      'driver': "",
                      'username': "vagrant",
                      'password': "vagrantvm",
                      'host': "localhost",
                      'port': "5432",
                      'dbname': "catalog"}

# Secret key for signing cookies
secrets_path = BASE_DIR + '/app/client_secrets.json'
CLIENT_ID = json.loads(
    open(secrets_path, 'r').read()
)['web']['client_id']

SECRET_KEY = CLIENT_ID
SECRET_PATH = secrets_path


class Config(object):
    DATABASE_URI = build_db_uri(DB_CONNECT_OPTIONS)
    SECRET_KEY = CLIENT_ID
    SECRET_PATH = secrets_path
    UPLOAD_FOLDER = BASE_DIR + "/app/static/images"
    STATIC_FOLDER = BASE_DIR + "/app/static"
    TEMPLATES_FOLDER = BASE_DIR + "/app/templates"
    SECRET_KEY = CLIENT_ID
    APPLICATION_NAME = "Catalog App"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = build_db_uri(DB_CONNECT_OPTIONS)


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
