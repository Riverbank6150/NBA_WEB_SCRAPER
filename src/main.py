from web_scraper import *
from url_parser import *



def main():

    url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"

    html_url_title = url_parse(url)

    soup = scrape_URL(url, html_url_title)

    parse(soup)

    # titles, stats, dataframe = parse(soup)
    dataframe = parse(soup)

    print_to_csv(html_url_title, dataframe)
    print_to_json(html_url_title, dataframe)
    print_to_xlsx(html_url_title, dataframe)
    print_to_parquet(html_url_title, dataframe)


if __name__ == "__main__":
    main()
