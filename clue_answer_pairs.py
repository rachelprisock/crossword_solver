# pseudo code this shit

# open the page http://www.xwordinfo.com/xml/Crossword/
# if <dir> open url (ex. http://www.xwordinfo.com/xml/Crossword/1942/)
#####now we're in the url for the year
# if .xml, store in item (all_years)
# else do nothing

##now we've parsed through the years and gained the .xml files for all years

# for each year in all_years
# parse clue, answer into all_pairs item


##from here, we have gained all clues and we can start to manipulate the data to structure it into a dictionary
##where the clue is the key and the answer or answers are a list that are the value of the key clue


# from bs4 import BeautifulSoup
# from urllib.request import urlopen
#
# html = urlopen("http://www.xwordinfo.com/xml/Crossword/")
# html_doc = html.read()
# #should specify what type of parser, in BeautifulSoup docs, they use 'html.parser' and terminal is using "lxml"
# soup = BeautifulSoup(html_doc)

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



## xml_links[0:5] = ['http://www.xwordinfo.com/xml/Crossword/1942/1942-01.xml', 'http://www.xwordinfo.com/xml/Crossword/1942/1942-02.xml', 'http://www.xwordinfo.com/xml/Crossword/1942/1942-03.xml', 'http://www.xwordinfo.com/xml/Crossword/1942/1942-04.xml', 'http://www.xwordinfo.com/xml/Crossword/1942/1942-05.xml']

clue_answer_pairs = {}

print(xml_links)
exit()

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

                    # Could always create another loop for if clue in clue_answer_pairs update ans to a list of itself and the previous asnwer
                    # don't know if I will have to go find the record where clue == clue and update ans

                    ######### REFACTOR #########
                    # Trying out xml parsing with one file
                    # blah = requests.get('http://www.xwordinfo.com/xml/Crossword/2015/2015-01.xml')
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
