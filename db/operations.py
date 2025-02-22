from .connection import engine  # 从同一包内的 connection.py 导入
from .models import Base  # 从同一包内的 models.py 导入


def create_tables():
    Base.metadata.create_all(bind=engine)


def drop_tables():
    # 谨慎使用！这会删除所有表！
    Base.metadata.drop_all(bind=engine)