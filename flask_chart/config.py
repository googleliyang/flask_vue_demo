# 导入redis模块
from redis import StrictRedis


class Config:
    DEBUG = None
    # 配置密钥
    SECRET_KEY = 'mMr88P+cvbxFXvcpX9PpiBTWMDLtGNkI7fwKhVv7GWuv9QZyRoyUsw=='

    # 配置数据库的链接
    # SQLALCHEMY_DATABASE_URI = 'mysql://python37_11:x864dxNPP2X4NnMk@149.129.106.112/python37_11'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1/demo_chart'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 
    # 配置状态保持session信息的存储
    SESSION_TYPE = 'redis'
    # 抽取redis的主机和端口
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT= 6379
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # SESSION_REDIS = StrictRedis(host='149.129.106.112', port=6379)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400


# 定义开发环境的配置类
class DevelopmentConfig(Config):
    DEBUG = True


# 定义生产环境的配置类
class ProductionConfig(Config):
    DEBUG = False


# 实现不同环境下的配置类的字典映射
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
