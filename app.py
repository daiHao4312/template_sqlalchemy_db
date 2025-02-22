from db import (
    create_tables,
    CollegeVolunteeringScoresModel,
    add_object,
    get_db,
    SessionLocal
)  # 从 db 包导入
from sqlalchemy.orm import Session
from exts import db  # 从 exts 包导入数据库会话
from utils.volunteerData_util import save_to_db  # 从 utils 包导入保存到数据库的函数


def initialize_database():
    """初始化数据库（创建表）"""
    create_tables()
    print("数据库初始化完成!")


def main():
    initialize_database()  # 初始化数据库

    try:
        # 保存一条数据到数据库
        data = {
            "speciality": "计算机科学与技术",
            "school_name": "北京大学",
            "avg_score": 90,
            "max_score": 100,
            "province": "北京",
            "category": "高校",
            "year": 2020,
            "batch": "2020级"
        }
        save_to_db(data)

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # 发生错误时回滚事务
    finally:
        db.close()  # 确保关闭会话


if __name__ == "__main__":
    main()
