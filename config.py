class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key'
    # Add other configuration settings here

class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific configurations
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/social-media-api'

class ProductionConfig(Config):
    # Production-specific configurations
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/dbname'

# Create an instance of the desired configuration class
api_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}