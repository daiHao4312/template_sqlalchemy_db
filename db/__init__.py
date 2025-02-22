# 这一行很重要, 导入这些模块，使它们可以通过 db 包直接访问
from .connection import engine, SessionLocal, get_db
from .models import Base, CollegeVolunteeringScoresModel  # 导入 User 模型
from .operations import create_tables, drop_tables
from .schema import (
    add_object,
    get_object_by_id,
    get_all_objects,
    update_object,
    delete_object  # 导入特定的操作函数
)
