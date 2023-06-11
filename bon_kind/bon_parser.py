from abc import ABC, abstractmehtod
from bon import Bon

class BonParser(ABC):
    @abstractmehtod
    @staticmethod
    def get_kind_indication() -> str:
        pass


    @abstractmehtod
    def parse_bon(self, bon_text) -> Bon:
        pass