class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, fio, email, phone, passport, username, password):
        if self.user_repository.get_user(username):
            return False  # Пользователь с таким логином уже существует

        # Создаем пользователя с дополнительной информацией
        new_user = UserModel(fio=fio, email=email, phone=phone, passport=passport, username=username, password=password)
        self.user_repository.save_user(new_user)
        return True

    def authenticate_user(self, username, password):
        user = self.user_repository.get_user(username)
        if user and user.password == password:
            return True
        return False