import sys
import argparse
from web_scraper import *

parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# CLI for output file type
parser.add_argument('-f', '--format', type=str, nargs='+',
                    help='output format for the file', default=['csv'])

# CLI for different URLs
# parser.add_argument('-o', '--output', type=str, nargs='+',
#                     help='an integer for the accumulator')

args = parser.parse_args()
# print(args.accumulate(args.integers))
print(args.format)




url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
soup = scrape_URL(url)
parse(soup)


for f in args.format:

    match(f):

        case "csv":

            print_to_csv()

        case "json":

            print_to_json()

        case "excel":

            print_to_xlsx()

        case "xlsx":

            print_to_xlsx()

        case "parquet":

            print_to_parquet()

parser.add_argument('-u', '--url', type=str, help= 'provide the url you would like to scrape',
                    default= ["https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"])
