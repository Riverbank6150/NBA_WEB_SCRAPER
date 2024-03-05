import csv

import bs4
import pandas as pd
import requests
# import sys
import argparse
#import pyarrow
import os

ROOT_DIR = os.path.dirname( os.path.abspath( __file__ ) )

def prepare_file_path( html_url_title: str, extension: str ) -> str:

    filename = os.path.join( ROOT_DIR,  html_url_title + extension )
    filename = os.path.abspath(filename)

    create_folder(filename)
    delete_file(filename)

    return filename

def create_folder(filename: str):

    dir_name = os.path.dirname(filename)

    if not os.path.exists( dir_name ):
        os.makedirs( dir_name )

def delete_file(filename: str):

    if os.path.exists( filename ):

        os.remove(filename)

def scrape_URL(url, html_url_title):
    # URL = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"

    page = requests.get(url)

    filename = prepare_file_path( html_url_title, ".html" )

    print( filename )

    with open(filename, "w", encoding='utf-8') as f:
        f.write(page.text)

    with open(filename, "r", encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    return soup

def parse(soup):
    # check with Mikey, made 'titles' and 'stats' global variables. Don't know how to call in a different way
    # global titles
    # global stats
    # global dataframe

    table = soup.find("table", id="per_game_stats")
    # find('tr') to find the first row, findAll('th') to find all column headers. If no findAll.('th'), newline characters given in between the column headers list.
    columns = table.find('tr').findAll('th')

    titles = []
    for column in columns[1:]:
        title = column.text
        titles.append(title)

    # What we want
    # print(titles)

    rows = table.findAll('tr')
    # List of all data cells in table for the players
    stats = []

    # Loop through each row (player name and stats) in html table
    for row in rows[1:]:
        # Temporary list to hold a singular player's data
        player_row = []
        # The amount of players (rows) in html table
        players = row.findAll('td')
        # Safety as headers are used in html table after every 20 players, making sure that the table is also not empty
        if players is not None and len(players) > 0:
            # Iterate through individual data cells for each player
            for player_data in players:
                # Add individual data cells to temporary list of single player's data
                player_row.append(player_data.text)
            # Add the temporary list to the master list of all data cells
            stats.append(player_row)

    dataframe = pd.DataFrame(stats, columns=titles)

    return dataframe

# What we want, each player having their stats in their own list within the large list of all the players
# print(stats)

# def print_to_csv(titles, stats):
#     with open('nba_2023_per_game_stats_alphabetical.csv', 'w', newline='', encoding='utf-8') as f:
#         w = csv.writer(f)
#         w.writerow(titles)
#         w.writerows(stats)

def print_to_csv(html_url_title, dataframe):
    # with open('nba_2023_per_game_stats_alphabetical.csv', 'w', newline='', encoding='utf-8') as f:
    filename = prepare_file_path( html_url_title, ".csv" )

    dataframe.to_csv(filename, encoding= 'utf-8', index= False)

def print_to_json(html_url_title, dataframe):
    # with open('nba_2023_per_game_stats_alphabetical.json', 'w', newline='', encoding='utf-8') as f:
    #     f.write(dataframe.to_json(orient="records", lines=True))

    filename = prepare_file_path( html_url_title, ".json" )

    dataframe.to_json(filename, orient= "records", lines=True)

def print_to_parquet(html_url_title, dataframe):
    filename = prepare_file_path( html_url_title, ".parquet" )

    dataframe.to_parquet(filename, compression='gzip')

def print_to_xlsx(html_url_title, dataframe):
    filename = prepare_file_path( html_url_title, ".xlsx" )

    dataframe.to_excel(filename, index=False)





# def command_line_interface():
    # to update, code from chatgpt
    #
    # args = sys.argv[1:]
    #
    # if not args:
    #     print("Usage: python main.py [argument]")
    #     sys.exit(1)
    #
    # argument = args[0]
    #
    # if argument == 'hello':
    #     print("Hello, user")
    # elif argument == 'help':
    #     print("This is a simple CLI program.")
    # else:
    #     print(f"Unknown argument: {argument}")
    # parser.add_argument('filename', nargs= '?',default= 'file1.txt', help= 'Filename of the file to process')
    # parser.add_argument('-c', '--copy', nargs= '?', default= '1', const= '2')
    # parser.add_argument('-s', '--something', action= 'store_true')

    # parser.add_argument('-n', '--name', default= 'file_copy', choices=['name1', 'name2'])



    #
    # parser = argparse.ArgumentParser(description= 'A program that scrapes NBA stats and produces the stats of each player in different file types', add_help= True)
    #
    #
    # parser.add_argument('-v', '--version', action= 'version', version= 'main.py v1.0')
    #
    # parser.add_argument('-ps', '--player_stat', metavar='player', type=str, help='Find certain stat value of certain player, usage: Firstname Lastname Stat Stats_page, eg "python src\main.py -ps Precious Achiuwa Tm NBA_2023_per_game" == TOR')
    # player = args.player
    #
    #
    # parser.add_argument('-ms', '--max_stat', help= 'Find max of a stat and which player reached it, usage: Stat Stats_page, eg "python src\main.py -ms PTS NBA_2023_per_game" == 33.1, Joel Embiid')
    #
    # arguments = parser.parse_args()
    # print(arguments)




