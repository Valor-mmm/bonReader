from bon_kind.bon_kinds import Kind
from datetime import datetime
from bon_item import BonItem

class Bon:
    def __init__(self, kind: Kind, date: datetime, bon_items: List[BonItem]):
        self.kind = kind,
        self.date = date
        self.bon_items = bon_items
