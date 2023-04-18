import python_weather
import asyncio

async def getWeather(location):
    async with python_weather.Client(format=python_weather.IMPERIAL) as client:
        weather = await client.get(location=location)

        print(weather.current.temperature)
        print(weather.current.local_time)
        print(weather.current.pressure)

        for forecast in weather.forecasts:
            print(forecast.date, forecast.astronomy)

            for hourly in forecast.hourly:
                print(f' --> {hourly!r}')

location = input('Give a your location: ')

asyncio.run(getWeather(location=location))
