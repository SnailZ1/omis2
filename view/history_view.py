import tkinter as tk

class HistoryView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

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

        # Отображение истории платежей
        self.display_payment_history()

    def display_payment_history(self):
        """Метод для отображения примеров истории платежей"""
        for payment in self.history:
            # Текст платежа
            payment_text = f"{payment['date']} - {payment['operation']} - {payment['amount']} ₽"

            # Создаем рамку для каждого платежа с голубым фоном
            payment_frame = tk.Frame(self, bg="#ADD8E6", bd=2, relief="solid", padx=10, pady=10, width=400)
            payment_frame.pack(fill="x", pady=5, padx=10)

            # Текст в рамке, выравнивание по левому краю
            payment_label = tk.Label(payment_frame, text=payment_text, font=("Arial", 12), bg="#ADD8E6", anchor="w")
            payment_label.pack(fill="x")
