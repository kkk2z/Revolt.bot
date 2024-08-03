import asyncio
import aiohttp
import revolt
from keep import keep_alive
print(f'ログインしました')
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
class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        if message.content == "過疎":
            await message.channel.send("俺は、24時間労働でいるけどな!")
class Client(revolt.Client):
    async def on_message(self, message: revolt.Message):
        if message.content == "kaso":
            await message.channel.send("俺は、24時間労働でいるけどな!")

async def main():
    async with aiohttp.ClientSession() as session:
        client = Client(session, "buNggYj1QbqhV0AU0y_flwes62oUPyuRHcdl-b2Jd8q3lwkJpFT268kDooa8RfvJ")
        await client.start()
# uoooo
keep_alive()#keepしてる。
os.system("kill")#ipアドレスをリセット
port = 5001 #ポート指定
asyncio.run(main())