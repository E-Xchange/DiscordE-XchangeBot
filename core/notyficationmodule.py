import time
import asyncio
import schedule
from databasemodule import takediscordid


def mainNotiSend(bot):
    def asyncloop():

        async def notyficationSend(id):
            time.sleep(1)
            await bot.wait_until_ready()
            user = await bot.fetch_user(id)
            await user.send("Your Notificate")

        async def loop():
            for i in takediscordid():
                await notyficationSend(i[0])

        bot.loop.create_task(loop())

    async def whilehehe():
        schedule.every().day.at("09:30").do(asyncloop)
        while True:
            schedule.run_pending()
            await asyncio.sleep(60)

    bot.loop.create_task(whilehehe())
