from urllib.parse import urlparse

def url_parse(url: str) -> str:

    # url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
    o = urlparse(url)

    # print(o.path)

    # url_path = url.split('/')
    # r = url_path[-1]
    # # print(r)
    #
    # s = r.split('.')
    # print(s[0])

    s = o.path.split(".")[0]

    if( s.startswith("/") ):
        return s[1:]

    return s

    # print(o.path)

# url_parse("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")
# url_parse("https://www.basketball-reference.com/leagues/NBA_2023_per_game.html")
# url_parse("https://www.basketball-reference.com/leagues/NBA_2024_per_game.html")
#
# url_parse("https://www.basketball-reference.com/teams/BOS/2024.html")
#
# url_parse("https://www.basketball-reference.com/players/h/holidjr01.html")
