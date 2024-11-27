import discord
from datetime import datetime
from dotenv import load_dotenv
import os

"""モジュール化"""
def run_discord_bot():
    #envファイルからTOKEN , ID の読み込み
    load_dotenv()

    TOKEN = os.getenv("TOKEN")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID"))  #https://discord.com/channels/{サーバーID}/{チャンネルID}


    #clientの作成と、その権限の付与
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f"ログイン完了 : {client.user}")
        #送信先のチャンネルの取得
        channel = client.get_channel(CHANNEL_ID)
        #正常にチャンネル取得できればメッセージ送信
        if channel:
            now = datetime.now()
            format_date = now.strftime("%m/%d %H:%M:%S")
            await channel.send(f"【{format_date}】 test massage")
        await client.close()

    #最終実行処理
    client.run(TOKEN)

"""シングル実行用"""
if __name__ == "__main__":
    run_discord_bot()
    