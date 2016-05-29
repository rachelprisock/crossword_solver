import xml.etree.ElementTree

import pandas as pd
import requests

from raw_xml_data import RawXmlData


class Lists(RawXmlData):
    def __init__(self):
        RawXmlData.__init__(self)
        # self.create_answer_list()
        # self.create_clue_list()
        self.create_clue_answer_list()

    # ## This method creates a csv of clues and number of times they appear to clue_list.csv
    # def create_clue_list(self):
    #     clue_list = {}
    #     print('Creating clue and appearance count document')
    #     for url in self.xml_links:
    #         link_content = requests.get(url).content
    #         tree = xml.etree.ElementTree.fromstring(link_content)
    #         print('Parsing url: ' + url)
    #         for child in tree:
    #             for child in child:
    #                 if child.tag == 'Clues':
    #                     for child in child:
    #                         clue = str(child.text)
    #                         clue = clue.replace('.', '').lower()
    #                         if clue not in clue_list:
    #                             clue_list[clue] = 0
    #                         elif clue in clue_list:
    #                             clue_list[clue] += 1
    #     clue_series = pd.Series(clue_list, name='TimesSeen')
    #     clue_series.index.name= 'Clue'
    #     clue_series.reset_index()
    #     clue_series.to_csv('clue_list.csv', header=True)
    # ## This method creates a csv of answers and number of times they appear called answer_list.csv
    # def create_answer_list(self):
    #     answer_list = {}
    #     print('Creating answer and appearance count document')
    #     for url in self.xml_links:
    #         link_content = requests.get(url).content
    #         tree = xml.etree.ElementTree.fromstring(link_content)
    #         print('Parsing url: ' + url)
    #         for child in tree:
    #             for child in child:
    #                 if child.tag == 'Clues':
    #                     for child in child:
    #                         ans = child.get('Ans').replace('.', '').lower()
    #                         if ans not in answer_list:
    #                             answer_list[ans] = 0
    #                         elif ans in answer_list:
    #                             answer_list[ans] += 1
    #     answer_series = pd.Series(answer_list, name='TimesSeen')
    #     answer_series.index.name= 'Answer'
    #     answer_series.reset_index()
    #     answer_series.to_csv('answer_list.csv', header=True)
    ## This method creates a csv of clue-answer pairs clue_answer_list.csv
    def create_clue_answer_list(self):
        global clue_answer_pairs
        clue_answer_pairs = {}
        print('Creating clue answer document')
        for url in self.xml_links[0:2]:
            link_content = requests.get(url).content
            tree = xml.etree.ElementTree.fromstring(link_content)
            print('Parsing url: ' + url)
            for child in tree:
                for child in child:
                    if child.tag == 'Clues':
                        for child in child:
                            clue = str(child.text)
                            clue = clue.replace('.', '').lower()
                            ans = child.get('Ans').replace('.', '').lower()
                            clue_answer_pairs.setdefault(clue, [])
                            clue_answer_pairs[clue].append(ans)
        clue_answer_df = pd.DataFrame(list(sorted(clue_answer_pairs.items())), columns=['clue', 'answers'])
        times_appeared = []
        for answer in clue_answer_df['answers']:
            times_appeared.append(len(answer))
        clue_answer_df['times_appeared'] = pd.Series(times_appeared, index=clue_answer_df.index)
        print(clue_answer_df)

        clue_df = pd.DataFrame()
        clue_df['clue'] = clue_answer_df['clue']
        print(clue_df)

        # clue_answer_df.to_csv('data_clue_answer_count.csv')

new = Lists()
