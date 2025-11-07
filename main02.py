#创建 API 接口，接收客户端发来的请求
from fastapi import FastAPI

app = FastAPI()

@app.get("/query1")
def read(page,id):
    return {"page":page,"limit": id}

@app.get("/query2")
def read(page:int,id=None):
    if id:
        return {"page":page,"limit": id}
    return{"page":page}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main02:app', host="127.0.0.1", port=8000,reload=True)