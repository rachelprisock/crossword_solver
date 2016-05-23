import re
import lxml
from robobrowser import RoboBrowser


def search_clue(clue, answer_length):
    browser = RoboBrowser(history=True)
    browser.open('http://www.dictionary.com/fun/crosswordsolver')

    form = browser.get_form(action='http://www.dictionary.com/fun/crosswordsolver')
    form
    form['query'] = clue
    form['l'] = str(answer_length)
    browser.submit_form(form)

    answer_confidence_dict = {}
    all_answers = browser.find_all('div', attrs={'class': 'matching-answer'})
    all_confidence = browser.find_all('div', attrs={'class': 'confidence'})

    # This prints all text from the row including the header 'Matching Answer'

    length = len(all_answers) - 1
    print(length)
    x = 1

    while x <= length:
        for answer in all_answers[x]:
            # answer = answer.text
            answer = answer.replace(' ', '').replace('\n', '').lower()
            for confidence in all_confidence[x]:
                # confidence = confidence.text
                confidence = confidence.replace('%', '').replace(' ', '').replace('\n', '')
                answer_confidence_dict[answer] = confidence
                x += 1
    print(answer_confidence_dict)
    print(len(answer_confidence_dict))

search_clue('all', 3)