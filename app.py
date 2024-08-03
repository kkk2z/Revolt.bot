import asyncio
import aiohttp
import revolt

#ここからメッセ送信
class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        if message.content == "浮上": #反応する言葉
            await message.channel.send("コンチャ")#返信する言葉
#ここまでがメッセ送信
class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        if message.content == "おはよう":
            await message.channel.send("おはようさん")

async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, "buNggYj1QbqhV0AU0y_flwes62oUPyuRHcdl-b2Jd8q3lwkJpFT268kDooa8RfvJ")
        await client.start()

asyncio.run(main())