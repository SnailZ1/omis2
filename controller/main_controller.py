class MainController:
    def __init__(self, factory, root):
        self.factory = factory
        self.root = root

        self.model = factory.create_model()
        self.view = factory.create_view(root)
        self.controller = factory.create_controller(self.model, self.view)

    def start(self):
        self.root.mainloop()
