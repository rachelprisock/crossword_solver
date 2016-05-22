## This file creates a csv of clue answer pairs and a count of
## how many times the clue appeared with all possible answers

### To Do:
    # Add answers into an array
    # If clue appears multiple times:
        # add new answer to answer array corresponding to clue (key)
        # Add new column in table to enumerate number of times clue appears
            # Could use len(answer_array) or something to populate that column.
            # Ex. # clue_answer_table = [[{ clue: [ans, ans, ans, ans]}], [len(answer_array)]]
        # Print final list to csv file.
        # Refactor first loop, quite messy
        # Take into account if a particular clue answer pair that is exactly the same appears
            # should also probably create a column to record the number of times this happens
            # but that will have to lie within the answer array potentially
            # ex. clue_answer_pair_table = [[{ clue: [ans[1], ans[5], ans, ans]}], [len(answer_array)]]

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
import requests
import xml.etree.ElementTree
from raw_xml_data import xml_links

class ClueAnswerPairs:
    clue_answer_pairs = {}

    # This block iterates through the xml_links list and populates a
    # dictionary of clue_answer_pairs from all years and all months
    print('Creating clue answer pair document')
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

