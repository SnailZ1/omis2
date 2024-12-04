class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.connect_view()

    def connect_view(self):
        pass
