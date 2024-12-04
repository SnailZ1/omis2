from abc import ABC, abstractmethod

class InterfaceFactory(ABC):
    @abstractmethod
    def create_model(self):
        pass

    @abstractmethod
    def create_view(self, root):
        pass

    @abstractmethod
    def create_controller(self, model, view):
        pass
