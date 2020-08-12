import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import argparse
def news(limit):
    URL = 'https://www.bbc.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    temp1 = []
    temp2 = []
    temp1 = soup.find_all('div', class_ = "media media--hero media--primary media--overlay block-link")
    temp2 = soup.find_all('div', class_ = "media media--overlay block-link")
    top_stories = temp1 + temp2
    if (limit!=None):
        top_stories = top_stories[:limit]
    L = []
    for story in top_stories:
        title = story.find('a', class_="media__link").text 
        L.append([title])
    print('\n')
    print("BBC")
    print(tabulate(L, headers = ["Title"], tablefmt = "fancy_grid"))


def print_urgent(limit = -1):
    URL = 'https://www.lorientlejour.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    urgent_results = soup.find_all('li', class_='urgent') #list of the elements that are of class urgent
    if limit != None:
        urgent_results = urgent_results[:limit]
    L = []
    for result in urgent_results:
        time = result.find('span', class_ = 'time').text
        title = result.find('p').find('span').text
        description = result.find('p').text.split("\xa0\xa0")[1]
        L.append([time,title, description])

    print(tabulate(L, headers = ["Time","Title", "Description"], tablefmt = "fancy_grid"))

def print_all(limit = -1):
    URL = 'https://www.lorientlejour.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    urgent_results1 = soup.find_all('div', class_= "latest-news-component desktop") 
    urgent_results = urgent_results1[0].find_all('li') #list of the elements that are of class urgent
    if limit != None:
        urgent_results = urgent_results[:limit]
    L = []
    for result in urgent_results:
        time = result.find('span', class_ = 'time').text
        title = result.find('p').find('span').text
        description = result.find('p').text.split("\xa0\xa0")[1]
        L.append([time,title, description])
    print(tabulate(L, headers = ["Time","Title", "Description"], tablefmt = "fancy_grid"))

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--type', action = 'store', required = True)
my_parser.add_argument('--limit', action = 'store', type = int)
args = my_parser.parse_args()
news(args.limit)
print('\n')
print("L'Orient-Le Jour")
if args.type == "urgent":
    print_urgent(args.limit)
elif args.type == "all":
    print_all(args.limit)
print('\n')