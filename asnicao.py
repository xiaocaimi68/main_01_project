import asyncio
import time

async def go():
    print("走走走")
    await asyncio.sleep(1)
    print("走到了")

async def run():
    print("跑跑跑")
    await asyncio.sleep(1)
    print("跑到了")

async def main():
    print("===开始走走走（异步模式）")
    start_time=time.time() #记录时间

#创建俩个异步任务，让他们同时进行
    tast1=asyncio.create_task(go())
    tast2=asyncio.create_task(run())

#等待俩个任务都完成
    await tast1
    await tast2

    sum_time=time.time() - start_time
    print(f"==完成！用时间：{sum_time:.2f}秒 ===")

if __name__=="__main__":
    asyncio.run(main())
