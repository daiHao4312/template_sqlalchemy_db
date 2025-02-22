from db import (
    create_tables,
    CollegeVolunteeringScoresModel,
    add_object,
    get_all_objects,
    get_db,
    SessionLocal
)  # 从 db 包导入
from exts import db  # 从 exts 包导入


# 保存一条数据到数据库
def save_to_db(data):
    """
    保存一条数据到数据库
    :param data:
    :return:
    """
    try:
        obj = CollegeVolunteeringScoresModel(**data)
        add_object(db, obj)
        return obj
    except Exception as e:
        print(f"保存数据到数据库失败: {e}")
        return None


# 使用 get_all_volunteering 函数从数据库中获取所有志愿数据
def get_all_volunteering():
    """获取所有用户"""
    try:
        return get_all_objects(db, CollegeVolunteeringScoresModel)
    except Exception as e:
        print(f"获取所有志愿数据失败: {e}")
        return None


