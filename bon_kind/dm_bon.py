from difflib import SequenceMatcher
from bon_kind.bon_parser import BonParser


def dm_bon_indication(bon_lines):
    largest_ratio = 0
    for line in bon_lines:
        line_ratio = SequenceMatcher(None, line, 'dm-drogerie-markt').ratio()
        largest_ratio = line_ratio
    return largest_ratio


class DMParser(BonParser):
    def __init__(self):
        pass

    @staticmethod
    def get_kind_indication(self):
        return 'dm-drogerie-markt'

    def parse_bon(self, bon_text) -> Bon:
        pass
