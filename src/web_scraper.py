import csv

import bs4
import pandas as pd
import requests


def scrape_URL(url):
    # URL = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"

    page = requests.get(url)

    filename = 'NBA_2023_per_game_stats_alphabetical.html'

    with open(filename, "w", encoding='utf-8') as f:
        f.write(page.text)

    with open(filename, "r", encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    return soup


def parse(soup):
    # check with Mikey, made 'titles' and 'stats' global variables. Don't know how to call in a different way
    global titles
    global stats
    global dataframe

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

# What we want, each player having their stats in their own list within the large list of all the players
# print(stats)

def print_to_CSV():
    with open('NBA_2023_per_game_stats_alphabetical.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(titles)
        w.writerows(stats)

def print_to_JSON():
    with open('NBA_2023_per_game_stats_alphabetical.json', 'w', newline='', encoding='utf-8') as f:
        f.write(dataframe.to_json(orient="records", lines=True))


def print_to_xlsx():
    dataframe.to_excel('NBA_2023_per_game_stats_alphabetical.xlsx', index=False)
