from crossword import Crossword
import crossword
import puz
import pandas as pd

class PuzzleSplitter:

    def __init__(self):
        self.split_puzzle()

    def read_puzzle(self):
        puz_object = puz.read('/Users/rachelprisock/Documents/Crosswords/NY_Time_Sat_Sample.puz')
        global puzzle
        puzzle = crossword.from_puz(puz_object)

    def get_across_answers(read_puzzle):
        #Across Answers
        word = []
        word_array = []
        global across_answers
        across_answers = []
        s_count = 1
        for x, y in puzzle.cells:
            if puzzle[x, y].solution != '.':
                word.append(puzzle[x, y].solution)
                if s_count % 15 == 0:
                    word_array.append(''.join(word).lower().split())
                    true_word_array = [x for x in word_array if x != []]
                    across_answers.append(true_word_array)
                    word_array = []
                    word = []
            elif puzzle[x, y].solution == '.':
                word_array.append(''.join(word).lower().split())
                true_word_array = [x for x in word_array if x != []]
                word = []
            s_count += 1

    def get_down_answers(read_puzzle):
        # Down Answers
        down_word = []
        down_word_array = []
        global down_answers
        down_answers = []
        d_count = 1
        x = 0
        y = 0
        for y, x in puzzle.cells:
            if y <= 14 and x <= 14:
                if puzzle[x, y].solution != '.':
                    down_word.append(puzzle[x, y].solution)
                    if d_count % 15 == 0:
                        down_word_array.append(''.join(down_word).lower().split())
                        true_down_word_array = [x for x in down_word_array if x != []]
                        down_answers.append(true_down_word_array)
                        down_word_array = []
                        down_word = []
                elif puzzle[x, y].solution == '.':
                    down_word_array.append(''.join(down_word).lower().split())
                    true_down_word_array = [x for x in down_word_array if x != []]
                    down_word = []
                else:
                    print('Things are broken')
                y = y + 1
                d_count += 1
            elif y > 14 >= x:
                y = 0
                x += 1
            elif x > 14 >= y:
                x = 0

    def create_clue_df(read_puzzle):
        # Create Clue DataFrame to add answers to
        clue_row = []
        all_clues = []
        for row in puzzle.clues.all():
            for item in row:
                if type(item) == str:
                    item = item.replace('.', '').lower()
                clue_row.append(item)
            all_clues.append(clue_row)
            clue_row = []
            global clue_answer_df
            clue_answer_df = pd.DataFrame(all_clues, columns=['direction', 'clue_number', 'clue'])

    def create_array_of_all_answers(self):
        # Create master array of all answers
        global all_answers
        all_answers = []
        all_answers.append(across_answers)
        all_answers.append(down_answers)

    def format_all_answers(self):
        # Break that array down into a format consumable enough to add to my DataFrame
        global true_all_answers
        global answer_length
        true_all_answers = []
        answer_length = []
        for set in all_answers:
            for row in set:
                for answer in row:
                    for word in answer:
                        true_all_answers.append(word)
                        answer_length.append(int(len(word)))

    def format_dfs(self):
        # Add Answers to DataFrame
        clue_answer_df['answer'] = pd.Series(true_all_answers, index=clue_answer_df.index)

        # Add Answer lengths to DataFrame
        clue_answer_df['answer_length'] = pd.Series(answer_length, index=clue_answer_df.index)

        global clue_answer_len_df
        clue_answer_len_df = pd.DataFrame(clue_answer_df, columns=['clue', 'answer_length'])
        self.clue_answer_len_df = clue_answer_len_df

    def split_puzzle(self):
        self.read_puzzle()
        self.get_across_answers()
        self.get_down_answers()
        self.create_clue_df()
        self.create_array_of_all_answers()
        self.format_all_answers()
        self.format_dfs()

        # print('This DF will be passed to the Solutions portion')
        # print(clue_answer_df)
        # print('This portion will be passed to the Modules')

        # print(clue_answer_len_df)
