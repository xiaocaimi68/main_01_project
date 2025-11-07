from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 定义 POST 接口接收的数据格式
class Item(BaseModel):
    name: str
    price: float

# 🟢 GET 接口：测试接口是否能访问
@app.get("/hello")
def say_hello():
    return {"message": "你好！FastAPI 正常运行中 🚀"}

# 🟡 POST 接口：提交 JSON 数据
#接口的路径
@app.post("/item")
def create_item(item: Item):
    return {"message": f"你创建了 {item.name}, 价格是 {item.price} 元"}
