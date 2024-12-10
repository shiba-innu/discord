# discord_bot.py
import discord
from datetime import datetime
from dotenv import load_dotenv
import os

TOKEN = os.getenv("TOKEN")

load_dotenv()


# Discord通知用関数
def run_discord_bot(channel_id, message):


    # clientの作成と、その権限の付与
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"ログイン完了 : {client.user}")
        # 送信先のチャンネルの取得
        channel = client.get_channel(channel_id)
        # 正常にチャンネル取得できればメッセージ送信
        if channel:
            now = datetime.now()
            format_date = now.strftime("%m/%d %H:%M:%S")
            await channel.send(f"【{format_date}】 {message}")
        await client.close()

    # 最終実行処理
    client.run(TOKEN)
