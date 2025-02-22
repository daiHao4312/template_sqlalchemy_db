from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# 创建数据库连接的
engine = create_engine(Config.DB_URI)
# 创建数据库会话的
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():  # 保持 get_db 函数不变
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()