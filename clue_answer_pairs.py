from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree
import pdb

# This block sets the stage for getting a list of links to the different years of crossword puzzles
home = requests.get('http://www.xwordinfo.com/xml/Crossword/').content
soup = BeautifulSoup(home, 'html.parser')
home_links = soup.find_all('a')
year_links = []
month_links = []
xml_links = []
clue_list = []
answer_list = []
clue_answer_pairs = {}

# This block gets a list called year_links with includes all links to different years of crossword puzzles
print('Init home links \n')
for link in home_links:
    link = link.get('href')
    if link.startswith('/xml/Crossword/'):
        link = 'http://www.xwordinfo.com' + link
        year_links.append(link)

# This block iterates through year_links and creates a list of all months links to crossword puzzles
print('Init year links')
for year in year_links:
    year_page = requests.get(year).content
    soup2 = BeautifulSoup(year_page, 'html.parser')
    month_links.append(soup2.find_all('a'))
    # This gives multiple arrays within an array

# This block iterates through lists month_links and creates a new list of all links to xml files to be parsed through
print('Init month links')
for set in month_links:
    for month in set:
        month = month.get('href')
        if month.startswith('/xml/Crossword/' + str(1)):
            month = 'http://www.xwordinfo.com' + month
            xml_links.append(month)
        elif month.startswith('/xml/Crossword/' + str(2)):
            month = 'http://www.xwordinfo.com' + month
            xml_links.append(month)
        else:
            print('Not writing parent directory link')

# This block iterates through the xml_links list and populates a
# dictionary of clue_answer_pairs from all years and all months
print('Init xml links')
for url in xml_links:
    link_content = requests.get(url).content
    tree = xml.etree.ElementTree.fromstring(link_content)
    for child in tree:
        for child in child:
            if child.tag == 'Clues':
                for child in child:
                    clue = child.text
                    ans = child.get('Ans')
                    clue_answer_pairs[clue] = ans


# This file parses the xml links on xwordinfo to gather a dictionary of clue answer pairs
# To Do:
    # When a clue appears multiple times, need to add a column to enumerate
        # the number of occurances of that clue
    # If a clue appears multiple times, add answer to array corresponding to clue
    # ex. [[{ apple: [ red, aday, worm]}], [3]]
        # clue_answer_table = [[{ clue: [ans, ans, ans, ans]}], [times_clue_appeared]]
    # make into useful methods to set up for creating answer table and clue table
    # refactor xml_links loop, messy structure.

######### One File Test #########
# Trying out xml parsing with one file
# clue_answer_pairs = {}# blah = requests.get('http://www.xwordinfo.com/xml/Crossword/2015/2015-01.xml')
# msg = blah.content
# tree = xml.etree.ElementTree.fromstring(msg)
# clue_answer_pairs = {}
# # And this set goes through the tree and creates a dictionary of clue answer pairs
# for child in tree:
#     for child in child:
#         if child.tag == 'Clues':
#             for child in child:
#                 clue = child.text
#                 ans = child.get('Ans')
#                 clue_answer_pairs[clue] = ans
# print(clue_answer_pairs)
