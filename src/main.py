from web_scraper import *
def main():
    URL = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
    # scrape_URL(URL)
    soup = scrape_URL(URL)
    parse(soup)
    print_to_CSV()

if __name__ == "__main__":
    main()
