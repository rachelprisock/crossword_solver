## This file creates a list of answers and number of times they appear
## Ex. answer = { answer: times_answer_appeared}

import requests
import xml.etree.ElementTree
from raw_xml_data import xml_links

class AnswerList:

    def create_answer_list(xml_links):
        answer_list = {}
        print('Creating answer and appearance count document')
        for url in xml_links:
            link_content = requests.get(url).content
            tree = xml.etree.ElementTree.fromstring(link_content)
            for child in tree:
                for child in child:
                    if child.tag == 'Clues':
                        for child in child:
                            ans = child.get('Ans')
                            if ans not in answer_list:
                                answer_list[ans] = 0
                            elif ans in answer_list:
                                answer_list[ans] += 1
    create_answer_list(xml_links)