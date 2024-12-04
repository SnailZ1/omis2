import tkinter as tk
from tkinter import messagebox


class AccountView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")

        # Список счетов
        self.accounts = [
            {"account_number": "123456789", "cards": [
                {"name": "Иван Иванов", "card_number": "1234 5678 9012 3456", "expiry": "12/24", "balance": 5000},
                {"name": "Мария Петрова", "card_number": "1234 5678 9012 3456", "expiry": "08/23", "balance": 1500},
            ]},
            {"account_number": "987654321", "cards": [
                {"name": "Сергей Сидоров", "card_number": "9876 5432 1098 7654", "expiry": "06/25", "balance": 1200},
            ]}
        ]

        # Создание виджетов
        self.create_widgets()

        # Устанавливаем размеры окна через AccountView
        self.config(width=800, height=600)

        # Обеспечиваем корректную растяжку внутри фрейма
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        # Заголовок окна
        label = tk.Label(self, text="Текущее состояние счетов", font=("Arial", 16))
        label.grid(row=0, column=0, pady=(20, 0))

        # Панель прокрутки
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollbar.grid(row=2, column=1, sticky="ns", padx=(0, 10))
        self.canvas.grid(row=2, column=0, pady=10, sticky="nsew")

        # Отображаем счета и карты
        self.create_account_widgets()

    def create_account_widgets(self):
        """Отображение счетов и карт"""
        row = 0
        for account in self.accounts:
            row = self.create_account_widget(account, row)

        # Кнопка "Добавить счет"
        add_account_button = tk.Button(self.scrollable_frame, text="Добавить счет", font=("Arial", 12), command=self.open_add_account_window)
        add_account_button.grid(row=row, column=0, pady=10)

    def create_account_widget(self, account, row):
        """Создание виджета для отображения счета и карт"""
        account_frame = tk.Frame(self.scrollable_frame, bg="#0056b3", bd=2, relief="solid", padx=10, pady=10)
        account_frame.grid(row=row, column=0, pady=10, sticky="ew", padx=20)

        account_label = tk.Label(account_frame, text=f"Номер счета: {account['account_number']}", font=("Arial", 14), fg="white", bg="#0056b3")
        account_label.grid(row=0, column=0, sticky="w", pady=5)

        # Кнопка "Добавить карту"
        add_card_button = tk.Button(account_frame, text="Добавить карту", font=("Arial", 10), command=lambda: self.open_add_card_window(account))
        add_card_button.grid(row=1, column=0, pady=5, sticky="w")

        # Отображение карт
        card_row = 2
        card_column = 0
        for card in account['cards']:
            self.create_card_widget(account_frame, card, card_row, card_column)
            card_column += 1
            if card_column > 3:
                card_column = 0
                card_row += 1

        return row + 1

    def create_card_widget(self, parent_frame, card, row, column):
        """Создание виджета для карты"""
        card_frame = tk.Frame(parent_frame, bg="#007bff", bd=2, relief="solid", padx=10, pady=10, width=150, height=120)
        card_frame.grid(row=row, column=column, padx=10, pady=10)

        name_label = tk.Label(card_frame, text=f"Владелец: {card['name']}", font=("Arial", 10), bg="#007bff", fg="white")
        name_label.grid(row=0, column=0, sticky="w", padx=10)

        card_number_label = tk.Label(card_frame, text=f"Номер карты: {card['card_number']}", font=("Arial", 10), bg="#007bff", fg="white")
        card_number_label.grid(row=1, column=0, sticky="w", padx=10)

        expiry_label = tk.Label(card_frame, text=f"Срок действия: {card['expiry']}", font=("Arial", 10), bg="#007bff", fg="white")
        expiry_label.grid(row=2, column=0, sticky="w", padx=10)

        balance_label = tk.Label(card_frame, text=f"Баланс: {card['balance']} Br", font=("Arial", 10), bg="#007bff", fg="white")
        balance_label.grid(row=3, column=0, sticky="w", padx=10)

    def open_add_account_window(self):
        """Открывает окно добавления счета"""
        add_account_window = tk.Toplevel(self)
        add_account_window.title("Добавить счет")
        add_account_window.geometry("300x200")

        tk.Label(add_account_window, text="Номер счета:", font=("Arial", 12)).pack(pady=5)
        account_number_entry = tk.Entry(add_account_window, font=("Arial", 12))
        account_number_entry.pack(pady=5)

        def add_account():
            account_number = account_number_entry.get()
            if account_number:
                self.accounts.append({"account_number": account_number, "cards": []})
                self.create_widgets()
                add_account_window.destroy()
            else:
                messagebox.showerror("Ошибка", "Введите номер счета!")

        tk.Button(add_account_window, text="Добавить", command=add_account).pack(pady=10)

    def open_add_card_window(self, account):
        """Открывает окно добавления карты"""
        add_card_window = tk.Toplevel(self)
        add_card_window.title("Добавить карту")
        add_card_window.geometry("300x250")

        tk.Label(add_card_window, text="Владелец карты:", font=("Arial", 12)).pack(pady=5)
        card_name_entry = tk.Entry(add_card_window, font=("Arial", 12))
        card_name_entry.pack(pady=5)

        tk.Label(add_card_window, text="Номер карты:", font=("Arial", 12)).pack(pady=5)
        card_number_entry = tk.Entry(add_card_window, font=("Arial", 12))
        card_number_entry.pack(pady=5)

        tk.Label(add_card_window, text="Срок действия (MM/YY):", font=("Arial", 12)).pack(pady=5)
        card_expiry_entry = tk.Entry(add_card_window, font=("Arial", 12))
        card_expiry_entry.pack(pady=5)

        def add_card():
            name = card_name_entry.get()
            card_number = card_number_entry.get()
            expiry = card_expiry_entry.get()

            if name and card_number and expiry:
                account["cards"].append({"name": name, "card_number": card_number, "expiry": expiry, "balance": 0})
                self.create_widgets()
                add_card_window.destroy()
            else:
                messagebox.showerror("Ошибка", "Все поля обязательны для заполнения!")

        tk.Button(add_card_window, text="Добавить", command=add_card).pack(pady=10)
