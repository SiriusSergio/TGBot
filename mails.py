import asyncio
import time


async def send_mail():
    print("Mail sending...")
    await asyncio.sleep(1)
    print("Mail send.")


async def main():
    mail_list = [send_mail() for _ in range(10)]
    await asyncio.gather(*mail_list)
    # asyncio.create_task(send_mail())
    # await asyncio.create_task(send_mail())


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
