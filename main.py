from tkinter import Tk
from factories.ui import UIFactory

def main():
    root = Tk()
    factory = UIFactory()

    # Создание компонентов
    start_window = factory.create_start_window(root)

    root.mainloop()

if __name__ == "__main__":
    main()
