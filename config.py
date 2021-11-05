class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = '63df4926bb9a41218025771acc1674f6'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}