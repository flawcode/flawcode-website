DEBUG = False
SECRET_KEY = 'secret-key'
EPISODE_COUNT = 11

# SQLAlchemy settings
DB_FILENAME = 'test'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DB_FILENAME+'.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Salts
SUBSCRIBE_TOKEN_SALT = 'subscribe-token-salt'
UNSUBSCRIBE_TOKEN_SALT = 'unsubscribe-token-salt'

# Email settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = ''

BASE_URL = 'localhost:5000'
