## This file creates a list of clues and number of times they appear
## Ex. clue_list = { clue: times_clue_appeared}

## To Do:
    # strip clues of periods, some early crosswords have periods at the end of the clue, but
        # could also connotate an abbreviation, which makes this a bit challenging...

import requests
import xml.etree.ElementTree
from raw_xml_data import xml_links

class ClueList:

    def create_clue_list(xml_links):
        clue_list = {}
        print('Creating clue and appearance count document')
        for url in xml_links:
            link_content = requests.get(url).content
            tree = xml.etree.ElementTree.fromstring(link_content)
            for child in tree:
                for child in child:
                    if child.tag == 'Clues':
                        for child in child:
                            clue = child.text
                            if clue not in clue_list:
                                clue_list[clue] = 0
                            elif clue in clue_list:
                                clue_list[clue] += 1
    create_clue_list(xml_links)
