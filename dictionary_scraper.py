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
        global final_answer_list
        global final_confidence_list
        answer_list = []
        answer_row = []
        confidence_list = []
        confidence_row = []
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
            print('storing results')
            all_answers = browser.find_all('div', attrs={'class': 'matching-answer'})
            all_confidence = browser.find_all('div', attrs={'class': 'confidence'})
            for answer in all_answers:
                answer = answer.text
                answer = answer.replace(' ', '').replace('\n', '').lower()
                answer_row.append(answer)
                while 'matchinganswer' in answer_row: answer_row.remove('matchinganswer')
                answer_list.append(answer_row)
                final_answer_list = [x for x in answer_list if x != []]
                answer_row = []
            for confidence in all_confidence:
                confidence = confidence.text
                confidence = confidence.replace('%', '').replace(' ', '').replace('\n', '')
                confidence_row.append(confidence)
                while 'Confidence' in confidence_row: confidence_row.remove('Confidence')
                confidence_list.append(confidence_row)
                final_confidence_list = [x for x in confidence_list if x != []]
                confidence_row = []

    def return_result_array(self):
        print(final_answer_list)
        print(final_confidence_list)
        all_answer_confidence_df = pd.DataFrame(self.clue_answer_length_array, columns=['clue', 'answer_length'])
        all_answer_confidence_df['candidates'] = pd.Series(answer_confidence_dict, index=all_answer_confidence_df.index)
        print(all_answer_confidence_df)

    def scrape_dictionary(self):
        self.search_clue()
        self.return_result_array()

    def query_with_puzzle_clues(self):
        global clue_answer_length_array
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
