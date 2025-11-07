from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 用于POST的数据模型
class User(BaseModel):
    name: str
    age: int

# GET 示例：通过查询参数获取数据
@app.get("/user")
def get_user(name: str, age: int):
    return {"method": "GET", "message": f"你好，{name}！你今年 {age} 岁。"}

# POST 示例：通过请求体提交数据
@app.post("/user")
def create_user(user: User):
    return {"method": "POST", "message": f"已创建用户：{user.name}, 年龄 {user.age}"}
