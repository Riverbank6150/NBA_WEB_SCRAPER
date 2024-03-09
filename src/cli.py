from main import *
from url_parser import *
from web_scraper import *

import argparse
import sys

# 'parser' variable initialized to parse through command-line arguments
# information of the project is given to the user
parser = argparse.ArgumentParser(
    prog='nba web scraper',
    description='provides files of scraped nba stats from www.basketball-reference.com')

# Initialization of specifications for the CLI for output file type
parser.add_argument('-f', '--format',
                    type=str,
                    nargs='+',
                    help='output format for the file',
                    default=['csv'])

# Initialization of specifications for the CLI for input url
parser.add_argument('-u', '--url',
                    type=str,
                    nargs='+',
                    help= 'provide the url you would like to scrape',
                    default= ["https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"])

# initializes 'args' variable to be used for cli usage
args = parser.parse_args()

# print statements to see arguments
print(args.format)
print(args.url)




# -----TO DO: CLI for allowing input of desired url to scrape-----
# decide how to initialize the 'url' variable to be used for the cli
# use 'html_url_title = url_parse(url)' and 'soup = scrape_URL(url, html_url_title)' to complete TO DO task?

# url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
# url = str(input("provide url you would like to scrape: "))
url = str

# use 'html_url_title = url_parse(url)' to complete TO DO task?
# initialize 'html_url_title' variable from ulr_parse function from url_parser.py file
html_url_title = url_parse(url)

# use 'soup = scrape_URL(url, html_url_title)' to complete TO DO task?
# 'soup' variable initialized from scrape_url function to be used in other functions
soup = scrape_URL(url, html_url_title)




# looks through 'format' arguments to decide which type of  file is created
for f in args.format:
    match f:

        case "csv":
            print_to_csv()

        case "json":
            print_to_json()

        case "parquet":
            print_to_parquet()

        case "xlsx":
            print_to_xlsx()
