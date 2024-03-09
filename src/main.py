from cli import *
from url_parser import *
from web_scraper import *

# main function to run the program
def main():

    # initialize 'url' variable as either default webpage or input from user
    url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
    # url = str(input("provide url you would like to scrape: "))


    # discontinued function (for now) to have 'url' as input from user and return 'url' variable to be used in main function
    # input_url()


    # initialize 'html_url_title' variable from ulr_parse function from url_parser.py file
    html_url_title = url_parse(url)

    # 'soup' variable initialized from scrape_url function to be used in other functions
    soup = scrape_URL(url, html_url_title)

    # function to create manageable dataframe from table referenced in html file
    dataframe = parse(soup)

    # function to produce csv file from dataframe created in parse function
    # 'html_url_title' variable used as title for the outputted csv file
    print_to_csv(html_url_title, dataframe)

    # function to produce json file from dataframe created in parse function
    # 'html_url_title' variable used as title for the outputted json file
    print_to_json(html_url_title, dataframe)

    # function to produce parquet file from dataframe created in parse function
    # 'html_url_title' variable used as title for the outputted parquet file
    print_to_parquet(html_url_title, dataframe)

    # function to produce xlsx file from dataframe created in parse function
    # 'html_url_title' variable used as title for the outputted xlsx file
    print_to_xlsx(html_url_title, dataframe)

# call for main function to run the program
if __name__ == "__main__":
    main()
