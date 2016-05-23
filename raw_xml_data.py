## This file parses xwordinfo to ultimately pull a list off all
## links to xml files, so a link to xml version of puzzles from
## all available years and all available months

from bs4 import BeautifulSoup
import requests

class RawXmlData:
    def __init__(self):
        self.gather_xml_data()

    # This block gets a list called year_links with includes all links to
    # different years of crossword puzzles
    def gather_xml_data(self):
        homepage = 'http://www.xwordinfo.com/xml/Crossword/'
        home = requests. get(homepage).content
        soup = BeautifulSoup(home, 'html.parser')
        home_a_tags = soup.find_all('a')
        year_links = []
        month_a_tags = []
        global xml_links
        xml_links = []


        print('Creating list of links to each year...')
        for link in home_a_tags:
            link = link.get('href')
            if link.startswith('/xml/Crossword/'):
                link = 'http://www.xwordinfo.com' + link
                year_links.append(link)

        # This block iterates through year_links and creates a list of
        # all months links to crossword puzzles
        print('Creating list of a tags corresponding to each month in each year...')
        for year in year_links:
            year_page = requests.get(year).content
            soup2 = BeautifulSoup(year_page, 'html.parser')
            month_a_tags.append(soup2.find_all('a'))
            # Structure: [[1991/02, 1991/03, etc], [1992/01, 1992/03, etc], [etc]]

        # This block iterates through lists month_links and creates a
        # new list of all links to xml files to be parsed through
        print('Creating list of links to each xml file for each month in each year')
        year_count = 1942
        for set in month_a_tags:
            for month in set:
                month = month.get('href')
                if month.startswith('/xml/Crossword/' + str(1)):
                    month = 'http://www.xwordinfo.com' + month
                    xml_links.append(month)
                elif month.startswith('/xml/Crossword/' + str(2)):
                    month = 'http://www.xwordinfo.com' + month
                    xml_links.append(month)
                else:
                    print('Added links for ' + str(year_count))
                    year_count += 1
        self.xml_links = xml_links