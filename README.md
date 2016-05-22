# crossword_solver

Parts:
1. Scraping:
  * Files devoted to scraping xwordinfo.com xml files of crossword puzzle data to gather clue, answer, and clue-answer pair files to populate a database
2. Organizer: 
  * Takes in crossword puzzles and sends the list of clues and answer length to each module and the grid information to the solver
3. Modules:
  1. Dictionary.com crossword clue look up site (http://www.dictionary.com/fun/crosswordsolver), input clue and answer length into query and gather answers in order of probability (as defined by them)
  2. Another crossword clue look up site, input clue and answer length into query and gather answers in order of probability (as defined by them)
  3. A module which simply queries the database and creates a candidate list. Orders based on probility based on how many times that clue, answer, or clue-answer pair had occurred.
  4. A final module that takes in all candidate lists and creates a final list to be sent to the crossword solver
4. Solver:
  * A crossword "solver" which attempts the candidates from the candidate list in the crossword grid and picks best answer based on which answers fit with the other answers in the grid.
5. Accuracy Test:
  * A final check to see how accurately the crossword puzzle was solved.