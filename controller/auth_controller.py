class AuthController:
    def __init__(self, auth_service, auth_view):
        self.auth_service = auth_service
        self.auth_view = auth_view
        self.connect_view()

    def connect_view(self):
        self.auth_view.on_login = self.on_login
        self.auth_view.on_register = self.on_register

    def on_login(self, username, password):
        # Логика обработки авторизации
        if self.auth_service.authenticate_user(username, password):
            self.auth_view.show_message("Авторизация успешна!")
            # Здесь можно перейти к следующему окну/виду
        else:
            self.auth_view.show_message("Неверный логин или пароль!")

    def on_register(self):
        # Здесь можно открыть окно регистрации
        self.auth_view.show_message("Переход к регистрации...")