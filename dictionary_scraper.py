############# CURRENT STATE ################
# Takes in the list of clue and answer_length
# from puzzle_splitter
# Queries each of those pairs and parses the list of
# results which comprise of answer and confidence
# Returns df of all scraped answers and confidence
# in relation to each clue and answer length
# to be send to the Candidate compiler

import re
import lxml
from robobrowser import RoboBrowser
import pandas as pd
from puzzle_splitter import PuzzleSplitter


class DictionaryScraper(PuzzleSplitter):
    def __init__(self):
        PuzzleSplitter.__init__(self)
        self.query_with_puzzle_clues()

    def search_clue(self):
        global count
        for row in self.clue_answer_length_array:
            clue = row[0]
            answer_length = row[1]
            global browser
            browser = RoboBrowser(history=True)
            print('Visiting dictionary.com search page')
            browser.open('http://www.dictionary.com/fun/crosswordsolver')
            form = browser.get_form(action='http://www.dictionary.com/fun/crosswordsolver')
            print('Enter in clue and answer_len')
            form['query'] = clue
            form['l'] = str(answer_length)
            browser.submit_form(form)
            self.store_results()

    def store_results(self):
        answer_row = []
        confidence_row = []
        global count
        print('storing results')
        all_answers = browser.find_all('div', attrs={'class': 'matching-answer'})
        all_confidence = browser.find_all('div', attrs={'class': 'confidence'})

        if len(all_answers) == 0 and len(all_confidence) == 0:
            answer_list.append(answer_row)
            confidence_list.append(confidence_row)

        for answer in all_answers:
            answer = answer.text
            if 'Matching Answer' not in answer:
                answer = answer.replace(' ', '').replace('\n', '').lower()
                answer_row.append(answer)
            elif 'Matching Answer' in answer:
                answer_list.append(answer_row)

        for confidence in all_confidence:
            confidence = confidence.text
            if 'Confidence' not in confidence:
                confidence = confidence.replace('%', '').replace(' ', '').replace('\n', '')
                confidence_row.append(confidence)
            else:
                confidence_list.append(confidence_row)

    def return_result_array(self):
        all_answer_confidence_df = pd.DataFrame(self.clue_answer_length_array, columns=['clue', 'answer_length'])
        all_answer_confidence_df['candidates'] = pd.Series(answer_list, index=all_answer_confidence_df.index)
        all_answer_confidence_df['confidence'] = pd.Series(confidence_list, index=all_answer_confidence_df.index)

    def scrape_dictionary(self):
        self.search_clue()
        self.return_result_array()

    def query_with_puzzle_clues(self):
        global clue_answer_length_array
        global answer_list
        global confidence_list
        answer_list = []
        confidence_list = []
        clue_answer_length_row = []
        clue_answer_length_array = []
        for index, row in self.clue_answer_len_df.iterrows():
            clue_answer_length_row.append(row[0])
            clue_answer_length_row.append(row[1])
            clue_answer_length_array.append(clue_answer_length_row)
            clue_answer_length_row = []
        self.clue_answer_length_array = clue_answer_length_array
        self.scrape_dictionary()

new = DictionaryScraper()
