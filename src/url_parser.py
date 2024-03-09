from cli import *
from main import *
from web_scraper import *

from urllib.parse import urlparse

def url_parse(url: str) -> str:

    # initialize 'url' variable as either default webpage or input from user
    url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
    # url = str(input("provide url you would like to scrape: "))

    # -----MIKEY CREATED - ASK FOR CLARIFICATION-----
    o = urlparse(url)

    # -----MIKEY CREATED - ASK FOR CLARIFICATION-----
    # when given url, parse through the url to return variable 's'
    s = o.path.split(".")[0]
    if s.startswith("/"):
        return s[1:]
    return s


    # discontinued code (for now), kept for future use if needed
    # print(o.path)
    # url_path = url.split('/')
    # r = url_path[-1]
    # # print(r)
    # s = r.split('.')
    # print(s[0])
    # print(o.path)


# discontinued code (for now) to see different outputs from different given urls
# url_parse("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")
# url_parse("https://www.basketball-reference.com/leagues/NBA_2023_per_game.html")
# url_parse("https://www.basketball-reference.com/leagues/NBA_2024_per_game.html")
# url_parse("https://www.basketball-reference.com/teams/BOS/2024.html")
# url_parse("https://www.basketball-reference.com/players/h/holidjr01.html")
