# auth_view.py

import tkinter as tk
from tkinter import messagebox
from config.ui_config import center_window

class AuthView:
    def __init__(self, root, open_main_window_callback=None):
        self.root = root
        self.open_main_window_callback = open_main_window_callback
        self.root.title("Авторизация")
        self.setup_window()

        # Поля для ввода логина и пароля
        self.username_label = tk.Label(self.root, text="Логин")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Пароль")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Кнопка для входа
        self.login_button = tk.Button(self.root, text="Войти", command=self.handle_login)
        self.login_button.pack(pady=20)

        # Кнопка для перехода в регистрацию
        self.register_button = tk.Button(self.root, text="Перейти к регистрации", command=self.open_register_window)
        self.register_button.pack(pady=5)

    def setup_window(self):
        """Настройка окна авторизации с учётом конфигурации"""
        center_window(self.root)

    def handle_login(self):
        """Обработка логина"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Логика проверки логина и пароля
        if username == "user" and password == "pass":  # Пример успешной проверки
            messagebox.showinfo("Успех", "Авторизация успешна!")
            self.open_main_window()  # Переход в главное окно после успешной авторизации
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")

    def open_main_window(self):
        """Переход в главное окно после успешной авторизации"""
        self.root.withdraw()  # Скрываем окно авторизации
        from view.main_window import MainWindow  # Импортируем главный экран внутри функции
        main_window = tk.Toplevel(self.root)  # Создаем главное окно
        main_view = MainWindow(main_window)  # Создаем представление главного окна
        main_window.deiconify()  # Показываем окно главного экрана

    def open_register_window(self):
        """Переход в окно регистрации"""
        self.root.destroy()  # Закрытие окна авторизации
        from view.register_view import RegisterView  # Импортируем регистрацию внутри функции
        register_window = tk.Tk()
        RegisterView(register_window)  # Переход к окну регистрации
        register_window.mainloop()
