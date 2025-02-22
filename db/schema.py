from typing import Type, List
from sqlalchemy.orm import Session
from .models import Base  # 从同一包内的 models.py 导入
from .connection import get_db  # 从同一包内的 connection.py 导入


def add_object(db: Session, obj: Base):
    """添加一个对象到数据库"""
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_object_by_id(db: Session, model: Type[Base], obj_id: int):
    """根据 ID 获取对象"""
    return db.query(model).filter(model.id == obj_id).first()


def get_all_objects(db: Session, model: Type[Base]) -> List[Base]:
    """获取模型的所有对象"""
    return db.query(model).all()


def update_object(db: Session, obj: Base):
    """更新对象（需要先修改对象的属性）"""
    db.commit()
    db.refresh(obj)  # 刷新以获取更新后的值
    return obj


def delete_object(db: Session, obj: Base):
    """删除对象"""
    db.delete(obj)
    db.commit()

# 可以添加更多特定于模型的数据库操作函数...
