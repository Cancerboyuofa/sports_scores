import requests
from bs4 import BeautifulSoup


def scrape_scores(sport, team):

    if sport == 'nfl':

        print("processing NFL Request")
        
        URL = "https://toolsyep.com/en/webpage-to-plain-text/?u=plaintextsports.com/nfl"
        html = requests.get(URL)

        soup = BeautifulSoup(html.content, 'html.parser')

        soup = soup.prettify()

        return soup
    
    elif sport == 'nba':

        print("Processing NBA Request")

        URL = "https://toolsyep.com/en/webpage-to-plain-text/?u=plaintextsports.com/nba"
        html = requests.get(URL)

        soup = BeautifulSoup(html.content, 'html.parser')

        soup = soup.prettify()

        return soup

    elif sport == 'mlb':

        print("Processing MLB Request")

        URL = "https://toolsyep.com/en/webpage-to-plain-text/?u=plaintextsports.com/mlb"

        html = requests.get(URL)

        soup = BeautifulSoup(html.content, 'html.parser')

        soup = soup.prettify()

        return soup
    
    elif team == "dbacks":

        print("Processing D-Backs Request")

        URL = "https://plaintextsports.com/mlb/2023/teams/arizona-diamondbacks"
        html = requests.get(URL)

        soup = BeautifulSoup(html.content, 'html.parser')

        soup = soup.prettify()

        return soup
    
    elif team == "raiders":

        print("Processing Raiders Request")

        URL = "https://plaintextsports.com/nfl/2023/teams/las-vegas-raiders"
        html = requests.get(URL)

        soup = BeautifulSoup(html.content, 'html.parser')

        soup = soup.prettify()

        return soup
    
    elif team == "suns":

        print("Processing Suns Request")

        URL = "https://plaintextsports.com/nba/2022-2023/teams/phoenix-suns"
        html = requests.get(URL)

        soup = BeautifulSoup(html.content, 'html.parser')

        soup = soup.prettify()

        return soup


    else:
        URL = "https://toolsyep.com/en/webpage-to-plain-text/?u=plaintextsports.com/"
        html = requests.get(URL)

        soup = BeautifulSoup(html.content, 'html.parser')

        soup = soup.prettify()

        return soup