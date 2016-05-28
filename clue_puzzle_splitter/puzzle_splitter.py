from crossword import Crossword
import crossword
import puz
import pandas as pd

puz_object = puz.read('/Users/rachelprisock/Documents/Crosswords/NY_Time_Sat_Sample.puz')
puzzle = crossword.from_puz(puz_object)

word = []
word_array = []
all_answers = []
s_count = 1
for x, y in puzzle.cells:
    if puzzle[x, y].solution != '.':
        word.append(puzzle[x, y].solution)
        if s_count % 15 == 0:
            word_array.append(''.join(word).lower().split())
            true_word_array = [x for x in word_array if x != []]
            row = (s_count // 15) - 1
            all_answers.append(true_word_array)
            word_array = []
            word = []
    elif puzzle[x, y].solution == '.':
        word_array.append(''.join(word).lower().split())
        true_word_array = [x for x in word_array if x != []]
        word = []
    s_count += 1
print(all_answers)

#across clue and number list to iterate over
clue_dict = {}
for number, clue in puzzle.clues.across():
    clue = clue.lower()
    clue = clue.replace('.', '')
    print(clue)
    clue_dict[number] = clue
    clue_dict_df = pd.DataFrame(list(sorted(clue_dict.items())), columns=['clue_number', 'clue'])

word_list = []
answer_length = []
for row in all_answers:
    for answer in row:
        for word in answer:
            word_list.append(word)
            answer_length.append(int(len(word)))

clue_dict_df['answer'] = pd.Series(word_list, index=clue_dict_df.index)

clue_dict_df['answer_length'] = pd.Series(answer_length, index=clue_dict_df.index)

print(clue_dict_df)

clue_dict_df.to_csv('solution_across_clue_answer_length.csv')