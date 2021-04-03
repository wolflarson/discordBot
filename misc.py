async def sendJoke(message):
    import json
    import aiohttp
    async with aiohttp.ClientSession() as session:
        jokeBaseURL = "https://api.chucknorris.io/jokes/random"
        # https://api.chucknorris.io/jokes/random [value]
        # https://icanhazdadjoke.com/ [joke] set header to "Accept: application/json"
        async with session.get(jokeBaseURL) as resp:
            getJokeObject = await resp.text()
            getJokeAsJSON = json.loads(getJokeObject)
#  this space needs to be here or it breaks lol wtf
    return getJokeAsJSON["value"]

async def sendWeather(message):
    import aiohttp
    # check if a city is set
    messageList = message.content.split(" ")
    isCitySet = len(messageList)
    if isCitySet > 1:
        city = message.content.split(" ")[1]
    else:
        city = "detroit"

    # create an empty string to hold the weather report
    weather = ""
    headers = {'content-type': 'text/plain'}
    async with aiohttp.ClientSession() as session:
        weatherBaseURL = "http://wttr.in/" + str(city) + "?T"
        # gather the full weather rport, split it line by line then just grab the first 6 lines
        async with session.get(weatherBaseURL,headers=headers) as resp:
            fullWeatherReport = await resp.text()
            split = fullWeatherReport.splitlines()
            count = 0
            for i in split:
                # this is the same as weather = weather + i in case I forget cuz I'm dumb
                weather += i
                weather += "\n"
                count += 1
                if count > 6:
                    break
    return weather