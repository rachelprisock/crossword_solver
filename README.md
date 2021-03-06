# crossword_solver

Parts:
- Scraping:
	- Files devoted to scraping xwordinfo.com xml files of crossword puzzle data to gather clue, answer, and clue-answer pair files to populate a database
- Organizer: 
	- Takes in crossword puzzles and sends the list of clues and answer length to each module and the grid information to the solver
- Modules:
	- Dictionary.com crossword clue look up site (http://www.dictionary.com/fun/crosswordsolver), input clue and answer length into query and gather answers in order of probability (as defined by them)
	- Another crossword clue look up site, input clue and answer length into query and gather answers in order of probability (as defined by them)
	- A module which simply queries the database and creates a candidate list. Orders based on probility based on how many times that clue, answer, or clue-answer pair had occurred.
	- A final module that takes in all candidate lists and creates a final list to be sent to the crossword solver
- Solver:
	- A crossword "solver" which attempts the candidates from the candidate list in the crossword grid and picks best answer based on which answers fit with the other answers in the grid.
- Accuracy Test:
	- A final check to see how accurately the crossword puzzle was solved.