import tkinter as tk

class AccountView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")
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

        # Пример таблицы счетов или данных
        account_info = tk.Label(self, text="Информация о текущих счетах и картах", font=("Arial", 12))
        account_info.grid(row=1, column=0, pady=10)

        # Пример данных карт
        self.accounts = [
            {"account_number": "123456789", "cards": [
                {"name": "Иван Иванов", "card_number": "1234 5678 9012 3456", "expiry": "12/24", "balance": 5000},
                {"name": "Мария Петрова", "card_number": "1234 5678 9012 3456", "expiry": "08/23", "balance": 1500},
                {"name": "Анна Кузнецова", "card_number": "1234 5678 9012 3456", "expiry": "05/25", "balance": 1200},
            ]},
            {"account_number": "987654321", "cards": [
                {"name": "Сергей Сидоров", "card_number": "9876 5432 1098 7654", "expiry": "06/25", "balance": 1200},
                {"name": "Татьяна Иванова", "card_number": "9876 5432 1098 7654", "expiry": "10/24", "balance": 3000},
            ]}
        ]

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

        # Ползунок прокрутки
        self.scrollbar.grid(row=2, column=1, sticky="ns", padx=(0, 10))
        self.canvas.grid(row=2, column=0, pady=10, sticky="nsew")

        # Отображаем счета и карты
        self.create_account_widgets()

    def create_account_widgets(self):
        """Отображение счетов и карт"""
        row = 0  # Начинаем с первой строки

        for account in self.accounts:
            row = self.create_account_widget(account, row)

    def create_account_widget(self, account, row):
        """Создание виджета для отображения счета и карт"""
        # Создаем рамку для счета
        account_frame = tk.Frame(self.scrollable_frame, bg="#0056b3", bd=2, relief="solid", padx=10, pady=10)
        account_frame.grid(row=row, column=0, pady=10, sticky="ew", padx=20)

        # Номер счета
        account_label = tk.Label(account_frame, text=f"Номер счета: {account['account_number']}", font=("Arial", 14), fg="white", bg="#0056b3")
        account_label.grid(row=0, column=0, sticky="w", pady=5)

        # Отображаем карты для данного счета
        card_row = 1  # Начинаем с первой строки внутри рамки
        card_column = 0  # Начинаем с первого столбца

        # Отображаем карты в строках, переходя на новую строку при переполнении
        for card in account['cards']:
            self.create_card_widget(account_frame, card, card_row, card_column)
            card_column += 1
            if card_column > 3:  # Если больше 3 карт, переходим на новую строку
                card_column = 0
                card_row += 1

        return row + 1  # Возвращаем следующую строку для следующего счета

    def create_card_widget(self, parent_frame, card, row, column):
        """Создание виджета для отображения информации о карте"""
        card_frame = tk.Frame(parent_frame, bg="#007bff", bd=2, relief="solid", padx=10, pady=10, width=150, height=120)
        card_frame.grid(row=row, column=column, padx=10, pady=10)

        # Имя владельца
        name_label = tk.Label(card_frame, text=f"Владелец: {card['name']}", font=("Arial", 10), bg="#007bff", fg="white")
        name_label.grid(row=0, column=0, sticky="w", padx=10)

        # Номер карты
        card_number_label = tk.Label(card_frame, text=f"Номер карты: {card['card_number']}", font=("Arial", 10), bg="#007bff", fg="white")
        card_number_label.grid(row=1, column=0, sticky="w", padx=10)

        # Срок действия
        expiry_label = tk.Label(card_frame, text=f"Срок действия: {card['expiry']}", font=("Arial", 10), bg="#007bff", fg="white")
        expiry_label.grid(row=2, column=0, sticky="w", padx=10)

        # Баланс
        balance_label = tk.Label(card_frame, text=f"Баланс: {card['balance']} Br", font=("Arial", 10), bg="#007bff", fg="white")
        balance_label.grid(row=3, column=0, sticky="w", padx=10)
