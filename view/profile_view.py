import tkinter as tk
from tkinter import messagebox


class ProfileView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Личный кабинет", font=("Arial", 16))
        label.pack(pady=20)

        # Информация о пользователе
        profile_info = tk.Label(self, text="Здесь можно изменить свои данные", font=("Arial", 12))
        profile_info.pack(pady=10)

        # Форма для ввода данных
        self.create_input_form()

    def create_input_form(self):
        """Создание формы для ввода данных пользователя"""

        # Создаем общий фрейм для разделения на левую и правую часть
        form_frame = tk.Frame(self)
        form_frame.pack(pady=20, padx=20, fill="x")

        # Левая часть: ФИО, Email, Телефон, Номер паспорта
        left_frame = tk.Frame(form_frame)
        left_frame.grid(row=0, column=0, padx=20, sticky="w")

        # ФИО
        self.fio_label = tk.Label(left_frame, text="ФИО:", font=("Arial", 12))
        self.fio_label.grid(row=0, column=0, pady=(10, 5), sticky="w")
        self.fio_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
        self.fio_entry.grid(row=0, column=1, pady=5, padx=10)
        # Пример заполнения ФИО
        self.fio_entry.insert(0, "Иванов Иван Иванович")

        # Email
        self.email_label = tk.Label(left_frame, text="Email:", font=("Arial", 12))
        self.email_label.grid(row=1, column=0, pady=(10, 5), sticky="w")
        self.email_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
        self.email_entry.grid(row=1, column=1, pady=5, padx=10)
        # Пример заполнения email
        self.email_entry.insert(0, "ivanov@mail.com")

        # Телефон
        self.phone_label = tk.Label(left_frame, text="Телефон:", font=("Arial", 12))
        self.phone_label.grid(row=2, column=0, pady=(10, 5), sticky="w")
        self.phone_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
        self.phone_entry.grid(row=2, column=1, pady=5, padx=10)
        # Пример заполнения номера телефона
        self.phone_entry.insert(0, "+7 (123) 456-78-90")

        # Номер паспорта
        self.passport_label = tk.Label(left_frame, text="Номер паспорта:", font=("Arial", 12))
        self.passport_label.grid(row=3, column=0, pady=(10, 5), sticky="w")
        self.passport_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
        self.passport_entry.grid(row=3, column=1, pady=5, padx=10)
        # Пример заполнения номера паспорта
        self.passport_entry.insert(0, "1234 567890")

        # Правая часть: Логин, Пароль
        right_frame = tk.Frame(form_frame)
        right_frame.grid(row=0, column=1, padx=20, sticky="w")

        # Логин
        self.login_label = tk.Label(right_frame, text="Логин:", font=("Arial", 12))
        self.login_label.grid(row=0, column=0, pady=(10, 5), sticky="w")
        self.login_entry = tk.Entry(right_frame, font=("Arial", 12), width=20)
        self.login_entry.grid(row=0, column=1, pady=5, padx=10)
        # Пример заполнения логина
        self.login_entry.insert(0, "user")

        # Новый пароль
        self.new_password_label = tk.Label(right_frame, text="Новый пароль:", font=("Arial", 12))
        self.new_password_label.grid(row=1, column=0, pady=(10, 5), sticky="w")
        self.new_password_entry = tk.Entry(right_frame, font=("Arial", 12), show="*", width=20)
        self.new_password_entry.grid(row=1, column=1, pady=5, padx=10)
        # Пример заполнения пароля
        self.new_password_entry.insert(0, "")

        # Кнопка "Сохранить"
        self.save_button = tk.Button(self, text="Сохранить изменения", font=("Arial", 12), bg="#0056b3", fg="white", command=self.save_changes)
        self.save_button.pack(pady=20)

    def save_changes(self):
        """Метод для обработки сохранения изменений"""
        # Получаем введенные данные
        fio = self.fio_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        passport = self.passport_entry.get()
        login = self.login_entry.get()
        new_password = self.new_password_entry.get()

        # Проверка на пустые поля
        if not fio or not email or not phone or not passport or not login or not new_password:
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля!")
            return

        # Сохранение данных (например, в базе данных или файле)
        # Здесь просто имитируем сохранение, например, выводим сообщение
        messagebox.showinfo("Успех", "Данные успешно сохранены!")

        # Очистить поля после сохранения
        self.clear_fields()

    def clear_fields(self):
        """Метод для очистки полей ввода"""
        self.fio_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.passport_entry.delete(0, tk.END)
        self.login_entry.delete(0, tk.END)
        self.new_password_entry.delete(0, tk.END)
