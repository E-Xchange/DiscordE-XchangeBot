import time
import asyncio
import schedule
from anomalymodule import checkAnomaly
from databasemodule import takediscordid


def mainNotiSend(bot):
    def asyncloop():

        async def notyficationSend(id):
            anomalyResult = checkAnomaly()
            if anomalyResult[1] is False:
                time.sleep(1)
                await bot.wait_until_ready()
                user = await bot.fetch_user(id)
                await user.send(f"The price of Bitcoin has changed from yesterday by {anomalyResult[0]}%")

        async def userIteration():
            for i in takediscordid():
                await notyficationSend(i[0])

        bot.loop.create_task(userIteration())

    async def timeLoop():
        schedule.every().day.at("09:00").do(asyncloop)
        while True:
            schedule.run_pending()
            await asyncio.sleep(10)

    bot.loop.create_task(timeLoop())
