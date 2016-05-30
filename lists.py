############ CURRENT STATE ###############
# returns df of clue, answer and answer probability
# to be sent to db_module

################ TO DO: ##################
# 1. Could be refactored a bit, got a bit messy in
#    attempting to format data


import xml.etree.ElementTree
import pandas as pd
import requests
from raw_xml_data import RawXmlData

class Lists(RawXmlData):
    def __init__(self):
        RawXmlData.__init__(self)
        self.run_lists()

    def run_lists(self):
        self.clue_answer()
        self.clue_answer_count()
        self.clue_count()
        self.clue_answer_probability()
        self.final_clue_answer_probability_list()

    def clue_answer(self):
        global clue_answer_list
        clue_answer_list = []
        clue_answer_row = []
        for url in self.xml_links[100:101]:
            link_content = requests.get(url).content
            tree = xml.etree.ElementTree.fromstring(link_content)
            print('Parsing url: ' + url)
            for child in tree:
                for child in child:
                    if child.tag == 'Clues':
                        for child in child:
                            clue = str(child.text)
                            clue = clue.replace('.', '').lower()
                            clue_answer_row.append(clue)
                            answer = child.get('Ans').replace('.', '').lower()
                            clue_answer_row.append(answer)
                            clue_answer_list.append(clue_answer_row)
                            clue_answer_row = []

    def clue_answer_count(self):
        global final_clue_answer_count_list
        clue_answer_count = []
        clue_answer_count_row = []
        final_clue_answer_count_list = []
        x = len(clue_answer_list) - 1
        while x >= 0:
            clue_answer_count_row.append(clue_answer_list[x])
            clue_answer_count_row.append(clue_answer_list.count(clue_answer_list[x]))
            clue_answer_count.append(clue_answer_count_row)
            clue_answer_count_row = []
            x = x - 1
        for i in clue_answer_count:
            if i not in final_clue_answer_count_list:
                final_clue_answer_count_list.append(i)

    def clue_count(self):
        global final_clue_count_list
        clue_list = []
        clue_count_row = []
        clue_count_list = []
        final_clue_count_list = []
        for row in clue_answer_list:
            clue_list.append(row[0])
        x = len(clue_list)  - 1
        while x >= 0:
            clue_count_row.append(clue_list[x])
            clue_count_row.append(clue_list.count(clue_list[x]))
            clue_count_list.append(clue_count_row)
            clue_count_row = []
            x = x - 1
        for i in clue_count_list:
            if i not in final_clue_count_list:
                final_clue_count_list.append(i)

    def clue_answer_probability(self):
        global clue_answer_probability_list
        clue_answer_seen_list = []
        clue_answer_seen_row = []
        for row in final_clue_answer_count_list:
            clue_answer_seen_row.append(row[0][0])
            clue_answer_seen_row.append(row[1])
            clue_answer_seen_list.append(clue_answer_seen_row)
            clue_answer_seen_row = []

        clue_seen_total_list = []
        for clue in final_clue_count_list:
            clue_seen_total_list.append(clue[0])
            clue_seen_total_list.append(clue[1])

        clue_answer_probability_list = []
        for pair in clue_answer_seen_list:
            clue = pair[0]
            clue_answer_count = pair[1]
            target = clue_seen_total_list.index(pair[0])
            clue_check = clue_seen_total_list[target]
            target = target + 1
            clue_seen_count = clue_seen_total_list[target]
            clue_answer_probability = clue_answer_count / clue_seen_count
            clue_answer_probability_list.append(clue_answer_probability)

    def final_clue_answer_probability_list(self):
        global clue_answer_df
        clue_answer_list = []
        clue_answer_row = []
        for row in final_clue_answer_count_list:
            clue_answer_row.append(row[0][0])
            clue_answer_row.append(row[0][1])
            clue_answer_list.append(clue_answer_row)
            clue_answer_row = []
        clue_answer_df = pd.DataFrame(clue_answer_list, columns=['clue', 'answer'])
        clue_answer_df['answer_probability'] = pd.Series(clue_answer_probability_list, index=clue_answer_df.index)
        self.clue_answer_df = clue_answer_df



