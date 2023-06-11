class BonItem:
    def __init__(self, name: str, quantity: int, price_per_item: double):
        self.name = name,
        self.similar_existing_product = BonItem._find_similar_name(name)
        self.quantity = quantity
        self.price_per_item = price_per_item


    @staticmethod
    def _find_similar_name(name: str) -> str:
        # TODO
        return name
