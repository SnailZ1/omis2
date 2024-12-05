import tkinter as tk
from tkinter import ttk


class HistoryView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.sort_ascending = False  # Начальное направление сортировки

    def create_widgets(self):
        label = tk.Label(self, text="История платежей", font=("Arial", 16))
        label.pack(pady=20)

        # Пример данных о платежах
        self.history = [
            {"date": "01/12/2024", "operation": "Пополнение счета", "amount": 5000},
            {"date": "02/12/2024", "operation": "Оплата счета", "amount": 1200},
            {"date": "03/12/2024", "operation": "Перевод между счетами", "amount": 3000},
            {"date": "04/12/2024", "operation": "Пополнение счета", "amount": 1500},
            {"date": "05/12/2024", "operation": "Оплата счета", "amount": 700},
        ]

        # Выпадающий список для выбора вида операций
        filter_label = tk.Label(self, text="Фильтровать по виду операции:", font=("Arial", 12))
        filter_label.pack(pady=5)

        self.filter_var = tk.StringVar()
        self.filter_var.set("Все операции")  # Значение по умолчанию

        filter_options = ["Все операции", "Пополнение счета", "Оплата счета", "Перевод между счетами"]
        filter_menu = ttk.Combobox(self, textvariable=self.filter_var, values=filter_options, state="readonly")
        filter_menu.pack(pady=5)
        filter_menu.bind("<<ComboboxSelected>>", lambda e: self.display_payment_history())

        # Кнопка для сортировки по дате
        self.sort_button = tk.Button(self, text="Сортировать по дате", font=("Arial", 10), command=self.sort_by_date)
        self.sort_button.pack(pady=10)

        # Фрейм для отображения истории платежей
        self.history_frame = tk.Frame(self)
        self.history_frame.pack(fill="both", expand=True, pady=10)

        # Отображение начальной истории платежей
        self.display_payment_history()

    def display_payment_history(self):
        """Метод для отображения отфильтрованной и отсортированной истории платежей"""
        # Очищаем предыдущее содержимое
        for widget in self.history_frame.winfo_children():
            widget.destroy()

        # Получаем выбранный фильтр
        filter_type = self.filter_var.get()

        # Фильтруем историю платежей
        filtered_history = [
            payment for payment in self.history
            if filter_type == "Все операции" or payment["operation"] == filter_type
        ]

        # Отображаем отфильтрованные записи
        for payment in filtered_history:
            payment_text = f"{payment['date']} - {payment['operation']} - {payment['amount']} ₽"

            # Создаем рамку для каждого платежа с голубым фоном
            payment_frame = tk.Frame(self.history_frame, bg="#ADD8E6", bd=2, relief="solid", padx=10, pady=10)
            payment_frame.pack(fill="x", pady=5, padx=10)

            # Текст в рамке, выравнивание по левому краю
            payment_label = tk.Label(payment_frame, text=payment_text, font=("Arial", 12), bg="#ADD8E6", anchor="w")
            payment_label.pack(fill="x")

    def sort_by_date(self):
        """Метод для сортировки истории платежей по дате с переключением направления"""
        # Переключаем направление сортировки
        self.sort_ascending = not self.sort_ascending

        # Сортируем историю
        self.history.sort(key=lambda x: x["date"], reverse=not self.sort_ascending)

        # Меняем текст кнопки в зависимости от направления сортировки
        if self.sort_ascending:
            self.sort_button.config(text="Сортировать по дате (сначала старые)")
        else:
            self.sort_button.config(text="Сортировать по дате (сначала новые)")

        # Обновляем отображение истории
        self.display_payment_history()
