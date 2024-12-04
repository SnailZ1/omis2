# start_window.py

import tkinter as tk
from view.auth_view import AuthView  # Импортируем представление для авторизации
from view.register_view import RegisterView  # Импортируем представление для регистрации
from config.ui_config import center_window

class StartWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Приложение")
        self.setup_window()

        # Логотип (если нужно)
        self.logo = tk.PhotoImage(file="assets/logo.png")  # Пример, если у вас есть логотип
        self.logo_label = tk.Label(self.root, image=self.logo)
        self.logo_label.pack(pady=50)

        # Кнопка для перехода в окно авторизации
        self.login_button = tk.Button(self.root, text="Авторизация", command=self.open_auth_window)
        self.login_button.pack(pady=20)

        # Кнопка для перехода в окно регистрации
        self.register_button = tk.Button(self.root, text="Регистрация", command=self.open_register_window)
        self.register_button.pack(pady=20)

    def setup_window(self):
        """Настройка начального окна с учётом конфигурации"""
        center_window(self.root)  # Центрируем окно

    def open_auth_window(self):
        """Открытие окна авторизации"""
        self.root.withdraw()  # Скрываем стартовое окно
        auth_window = tk.Toplevel(self.root)  # Окно авторизации
        auth_view = AuthView(auth_window)  # Создаем представление авторизации
        auth_window.deiconify()  # Показываем новое окно

    def open_register_window(self):
        """Открытие окна регистрации"""
        self.root.withdraw()  # Скрываем стартовое окно
        register_window = tk.Toplevel(self.root)  # Окно регистрации
        register_view = RegisterView(register_window)  # Создаем представление регистрации
        register_window.deiconify()  # Показываем новое окно
