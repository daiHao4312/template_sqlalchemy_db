
class Config:
    """
    配置类
    """
    # 数据库配置信息
    HOSTNAME = '127.0.0.1'
    PORT = 3306
    DATABASE = 'db_voluntary_train_data'
    USERNAME = 'root'
    PASSWORD = '13084426786dcl'
    DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'