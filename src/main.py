from web_scraper import *


def main():
    url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
    soup = scrape_URL(url)
    parse(soup)

    print_to_csv()
    print_to_json()
    print_to_xlsx()
    print_to_parquet()


if __name__ == "__main__":
    main()
