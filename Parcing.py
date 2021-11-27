import xlsxwriter
import requests
from bs4 import BeautifulSoup as BS


def parse():
    URL = 'https://visualobjects.com/pl/web-design'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    response = requests.get(URL, HEADERS)
    soup = BS(response.content, 'html.parser')
    items = soup.findAll('div', class_='details-wrapper basic')
    links = []

    for item in items:
        links.append({
            'title': item.find('a', class_='details-title').get('href')
        })

    for link in links:
        link = str(link)
        print(link)

    #row = 0
    #workbook = xlsxwriter.Workbook('saver.xlsx')
    #worksheet = workbook.add_worksheet()

    # for col, data in enumerate(links):
        #worksheet.write_column(row, col, data)

    with open("Results.txt", "w") as file:
        for link in links:
            print(link, file=file, sep="\n \n")


parse()
