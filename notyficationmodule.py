import time
import asyncio
import schedule
from anomalymodule import checkAnomaly
from databasemodule import takediscordid


def mainNotiSend(bot):
    def asyncloop():

        async def notyficationSend(id):
            if checkAnomaly()[1] is False:
                time.sleep(1)
                await bot.wait_until_ready()
                user = await bot.fetch_user(id)
                await user.send(f"price change of {checkAnomaly()[0]}%")

        async def userIteration():
            for i in takediscordid():
                await notyficationSend(i[0])

        bot.loop.create_task(userIteration())

    async def timeLoop():
        # schedule.every().day.at("20:35").do(asyncloop)
        schedule.every(10).seconds.do(asyncloop)
        while True:
            schedule.run_pending()
            await asyncio.sleep(60)

    bot.loop.create_task(timeLoop())
