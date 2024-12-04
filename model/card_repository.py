class CardRepository:
    def __init__(self):
        self.cards = []

    def save_card(self, card):
        self.cards.append(card)

    def get_card(self, card_number):
        for card in self.cards:
            if card.card_number == card_number:
                return card
        return None