import json
import aiohttp
from html.parser import HTMLParser
import urllib.request

class Parser(HTMLParser):
    def __init__(self):
        self.links = []
        super().__init__()

    def handle_starttag(self, tag, attrs):
        listOfLinks = ""
        # Only parse the 'anchor' tag.
        if tag == "a":
            for name,link in attrs:
                if name == "href" and link.startswith("http") and not "google" in link:
                    self.links.append(link)

async def googleSearch(message):
    if message == "":
        return("Check !help")

    # basically right from https://www.askpython.com/python-modules/htmlparser-in-python
    baseURL = "https://www.google.com/search?q="
    userSearch = message.replace(" ", "+")
    url = baseURL + userSearch
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0'
        }
    )
    #Import HTML from a URL
    url = urllib.request.urlopen(req)
    fullHTML = url.read().decode()
    url.close()

    parser = Parser()
    parser.feed(fullHTML)
    return parser.links[0]

async def ddgSearch(message):
    if message == "":
        return("Check !help")

    baseURL = "https://duckduckgo.com/?q="
    userSearch = message.replace(" ", "+")
    url = baseURL + userSearch
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0'
        }
    )
    #Import HTML from a URL
    url = urllib.request.urlopen(req)
    fullHTML = url.read().decode()
    url.close()
    print(fullHTML)
    parser = Parser()
    parser.feed(fullHTML)
    # return parser.links[0]
    return("ddg's webpages are a mess. this needs work")

async def sendJoke():
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
    if message == "none":
        city = "detroit"
    else:
        city = message

    # create an empty string to hold the weather report
    #weather = ""
    headers = {'content-type': 'text/plain'}
    async with aiohttp.ClientSession() as session:
        weatherBaseURL = "http://wttr.in/" + str(city) + "?format=3"  #?T would remove color
        # gather the full weather rport, split it line by line then just grab the first 6 lines
        async with session.get(weatherBaseURL,headers=headers) as resp:
            fullWeatherReport = await resp.text()
            # this was required when we pulled the ASII art but discord butchers it so we changed the format for now
            # split = fullWeatherReport.splitlines()
            # count = 0
            # for i in split:
            #     # this is the same as weather = weather + i in case I forget cuz I'm dumb
            #     weather += i
            #     weather += "\n"
            #     count += 1
            #     if count > 6:
            #         break
    return fullWeatherReport

async def btc():
    price = ""
    async with aiohttp.ClientSession() as session:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin?localization=en&tickers=true&market_data=false&community_data=false&developer_data=false&sparkline=false"
        async with session.get(url) as resp:
            htmlResponse = await resp.text()
            getBTCAsJSON = json.loads(htmlResponse)
            for item in getBTCAsJSON.get('tickers',[]):
                if item['market']['identifier'] == 'gdax' and item['trade_url'] == "https://pro.coinbase.com/trade/BTC-USD":
                    price = item['market']['name'] + " $" + str(item['last'])

    return(price)