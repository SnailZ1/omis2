# register_view.py

import tkinter as tk
from tkinter import messagebox
from config.ui_config import center_window
from view.auth_view import AuthView  # Импортируем класс для авторизации

class RegisterView:
    def __init__(self, root):
        self.root = root
        self.root.title("Регистрация")
        self.setup_window()

        # Первый этап регистрации - вводим ФИО, email, телефон, паспортные данные
        self.step = 1  # Первый этап
        self.user_data = {}

        self.create_first_step()

    def setup_window(self):
        """Настройка окна регистрации с учётом конфигурации"""
        center_window(self.root)  # Центрируем окно

    def create_first_step(self):
        """Создаём элементы первого этапа регистрации"""
        # Удаляем предыдущие элементы, если они существуют
        self.clear_window()

        # Поля первого этапа
        self.fio_label = tk.Label(self.root, text="ФИО")
        self.fio_label.pack(pady=5)
        self.fio_entry = tk.Entry(self.root)
        self.fio_entry.pack(pady=5)

        self.email_label = tk.Label(self.root, text="Email")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        self.phone_label = tk.Label(self.root, text="Телефон")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack(pady=5)

        self.passport_label = tk.Label(self.root, text="Номер паспорта")
        self.passport_label.pack(pady=5)
        self.passport_entry = tk.Entry(self.root)
        self.passport_entry.pack(pady=5)

        # Кнопка для перехода ко второму этапу
        self.next_step_button = tk.Button(self.root, text="Далее", command=self.go_to_second_step)
        self.next_step_button.pack(pady=20)

        # Кнопка для отмены регистрации
        self.cancel_button = tk.Button(self.root, text="Отмена", command=self.cancel)
        self.cancel_button.pack(pady=5)

    def create_second_step(self):
        """Создаём элементы второго этапа регистрации"""
        # Удаляем предыдущие элементы, если они существуют
        self.clear_window()

        # Поля второго этапа
        self.username_label = tk.Label(self.root, text="Логин")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Пароль")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Кнопка для завершения регистрации
        self.register_button = tk.Button(self.root, text="Завершить регистрацию", command=self.complete_registration)
        self.register_button.pack(pady=20)

        # Кнопка для отмены регистрации
        self.cancel_button = tk.Button(self.root, text="Отмена", command=self.cancel)
        self.cancel_button.pack(pady=5)

    def go_to_second_step(self):
        """Перевод на второй этап регистрации (ввод логина и пароля)"""
        # Сохраняем данные первого этапа
        self.user_data['fio'] = self.fio_entry.get()
        self.user_data['email'] = self.email_entry.get()
        self.user_data['phone'] = self.phone_entry.get()
        self.user_data['passport'] = self.passport_entry.get()

        # Проверка, что все поля первого этапа заполнены
        if all([self.user_data[key] for key in ['fio', 'email', 'phone', 'passport']]):
            # Переход ко второму этапу
            self.create_second_step()  # Создаем элементы второго этапа
        else:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля первого этапа")

    def complete_registration(self):
        """Завершение регистрации"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            # Сохраняем логин и пароль
            self.user_data['username'] = username
            self.user_data['password'] = password

            # Логика для завершения регистрации (например, сохранение в базе данных)
            messagebox.showinfo("Успех", "Регистрация завершена!")

            # Закрываем окно регистрации
            self.root.destroy()

            # Переход в окно авторизации
            self.open_auth_window()

        else:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля второго этапа")

    def open_auth_window(self):
        """Создание и отображение окна авторизации"""
        auth_window = tk.Tk()
        auth_view = AuthView(auth_window)  # Создаем экземпляр окна авторизации
        auth_window.mainloop()

    def cancel(self):
        """Закрытие окна регистрации"""
        self.root.destroy()  # Закрытие окна авторизации

    def clear_window(self):
        """Очистка окна от всех виджетов"""
        for widget in self.root.winfo_children():
            widget.destroy()
