from db import get_db  # 从 db 包导入
from sqlalchemy.orm import Session

db: Session = next(get_db())  # 获得数据库连接

# 创建一个数据库会话. 两种方法都可以
# 方法1: 使用 get_db
# db1: Session = next(get_db())

# 方法2：使用 SessionLocal 直接创建
# db2 = SessionLocal()
