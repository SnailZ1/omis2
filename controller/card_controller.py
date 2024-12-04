class CardController:
    def __init__(self, card_service, card_view):
        self.card_service = card_service
        self.card_view = card_view
        self.connect_view()

    def connect_view(self):
        self.card_view.on_add_card = self.on_add_card
        self.card_view.on_get_card = self.on_get_card

    def on_add_card(self, card_number, card_type):
        if self.card_service.add_card(card_number, card_type):
            self.card_view.show_message("Карта добавлена успешно!")
        else:
            self.card_view.show_message("Ошибка при добавлении карты.")

    def on_get_card(self, card_number):
        card = self.card_service.get_card(card_number)
        if card:
            self.card_view.show_card_details(card)
        else:
            self.card_view.show_message("Карта не найдена.")