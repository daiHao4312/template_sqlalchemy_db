# template_sqlalchemy_db
python的sqlalchemy库连接数据库的模板



## 安装依赖

```
pip install -r requirements.txt
```

> 我的python版本是3.10.x



## 配置数据库参数

在config文件中：

```python
class Config:
    """
    配置类
    """
    # 数据库配置信息
    HOSTNAME = '127.0.0.1' # 地址
    PORT = 3306 # 端口号
    DATABASE = '数据库名'
    USERNAME = '用户名'
    PASSWORD = '密码'
    DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4'
```



## 创建数据库表

1. 在db文件夹下的`models.py`中，使用类的方法创建
2. 在同文件夹下的`__init__`中导入创建的类



## 修改数据库中的表

在db文件夹下的`schema.py`中有专门修改表的统一函数，你也可以自己写



修改数据库有两种方法，可以直接传入一个对象，要求字段必须和表中的字段一样

还有一种就是直接每个字段对应着写

```python
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
```

