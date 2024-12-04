class CardService:
    def __init__(self, card_repository):
        self.card_repository = card_repository

    def add_card(self, card_number, card_type):
        card = CardModel(card_number, card_type)
        self.card_repository.save_card(card)
        return True

    def get_card(self, card_number):
        return self.card_repository.get_card(card_number)