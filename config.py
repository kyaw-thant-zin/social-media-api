class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key'
    # Add other configuration settings here

class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific configurations

class ProductionConfig(Config):
    # Production-specific configurations
    pass

# Create an instance of the desired configuration class
api_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}