class UserRepository:
    def __init__(self):
        self.users = []

    def save_user(self, user):
        self.users.append(user)

    def get_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None