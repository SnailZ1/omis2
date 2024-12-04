from model.user_repository import UserRepository
from model.account_repository import AccountRepository
from model.card_repository import CardRepository
from model.payment_repository import PaymentRepository
from model.auth_service import AuthService
from model.account_service import AccountService
from model.payment_service import PaymentService
from model.card_service import CardService
from view.start_window import StartWindow
from view.auth_view import AuthView
from view.account_view import AccountView
from view.payment_view import PaymentView
from view.history_view import HistoryView
from controller.auth_controller import AuthController
from controller.account_controller import AccountController
from controller.payment_controller import PaymentController
from controller.card_controller import CardController

class UIFactory:

    def create_start_window(self, root):
        return StartWindow(root)
    def create_auth_view(self, root):
        return AuthView(root)

    def create_account_view(self, root):
        return AccountView(root)

    def create_payment_view(self, root):
        return PaymentView(root)

    def create_card_view(self, root):
        return HistoryView(root)

    def create_user_repository(self):
        return UserRepository()

    def create_account_repository(self):
        return AccountRepository()

    def create_card_repository(self):
        return CardRepository()

    def create_payment_repository(self):
        return PaymentRepository()

    def create_auth_service(self, user_repository):
        return AuthService(user_repository)

    def create_account_service(self, account_repository):
        return AccountService(account_repository)

    def create_payment_service(self, payment_repository, account_service):
        return PaymentService(payment_repository, account_service)

    def create_card_service(self, card_repository):
        return CardService(card_repository)

    def create_auth_controller(self, auth_service, auth_view):
        return AuthController(auth_service, auth_view)

    def create_account_controller(self, account_service, account_view):
        return AccountController(account_service, account_view)

    def create_payment_controller(self, payment_service, payment_view):
        return PaymentController(payment_service, payment_view)

    def create_card_controller(self, card_service, card_view):
        return CardController(card_service, card_view)