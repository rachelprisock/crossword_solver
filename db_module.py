from raw_xml_data import RawXmlData
from lists import Lists

class DbModule(Lists):

    def __init__(self):
        Lists.__init__(self)
        self.double_check()

    def double_check(self):
        print(self.clue_answer_df)


new = DbModule()