from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CollegeVolunteeringScoresModel(Base):
    __tablename__ = "college_volunteering_scores"
    # index=True 建立索引, autoincrement=True 自动递增
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    speciality = Column(String(255))  # 专业
    school_name = Column(String(255))  # 学校名称
    avg_score = Column(Integer)  # 平均分
    max_score = Column(Integer)  # 最高分
    province = Column(String(255))  # 考生地区
    category = Column(String(255))  # 科别
    year = Column(Integer)  # 年份
    batch = Column(String(255))  # 批次

