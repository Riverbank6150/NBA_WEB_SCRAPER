from web_scraper import *


def main():
    url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
    soup = scrape_URL(url)
    parse(soup)
    print_to_JSON()
    print_to_xlsx()


if __name__ == "__main__":
    main()
