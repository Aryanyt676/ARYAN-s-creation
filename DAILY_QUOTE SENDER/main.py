import random
import telegram as tlg
import asyncio

api_token=""#enter your api from telegram bot father
ChAT_ID=""#enter you chat id by https://api.telegram.org/bot<YOUR_API_TOKEN>/getUpdates
async def sendmessage(quote):
    bot=tlg.Bot(token=api_token)
    await bot.sendMessage(chat_id=ChAT_ID,text=quote)


def readfile():
    with open ("quote.txt",encoding="utf-8") as f:
        lines=f.readlines()
        randome_line=random.randint(1,len(lines)-1)
        quote=lines[randome_line]
        return quote

a=readfile()
asyncio.run(sendmessage(a))