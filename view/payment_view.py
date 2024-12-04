import tkinter as tk


class PaymentView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Платежи", font=("Arial", 16))
        label.pack(pady=20)

        # Пример текста, который поясняет возможность выполнения платежей
        payment_info = tk.Label(self, text="Здесь можно сделать платежи", font=("Arial", 12))
        payment_info.pack(pady=10)

        # Создаем выпадающий список для выбора типа операции
        self.operation_label = tk.Label(self, text="Выберите операцию", font=("Arial", 12))
        self.operation_label.pack(pady=10)

        self.operation_var = tk.StringVar()
        self.operation_var.set("Пополнение счета")  # Значение по умолчанию

        operation_options = [
            "Пополнение счета",
            "Оплата счета",
            "Перевод между счетами"
        ]

        self.operation_menu = tk.OptionMenu(self, self.operation_var, *operation_options)
        self.operation_menu.pack(pady=10)

        # Поле ввода для суммы
        self.amount_label = tk.Label(self, text="Введите сумму", font=("Arial", 10))
        self.amount_label.pack(pady=5)

        self.amount_entry = tk.Entry(self, font=("Arial", 10))
        self.amount_entry.pack(pady=5)

        # Кнопка для выполнения операции
        self.execute_button = tk.Button(self, text="Выполнить", font=("Arial", 10), bg="#4CAF50", fg="white",
                                        command=self.execute_payment)
        self.execute_button.pack(pady=20)

        # Метка для отображения результатов
        self.result_label = tk.Label(self, text="", font=("Arial", 12), fg="green")
        self.result_label.pack(pady=10)

    def execute_payment(self):
        """Обработчик выполнения платежа"""
        operation_type = self.operation_var.get()
        amount = self.amount_entry.get()

        # Проверка, что сумма введена корректно
        if not amount.isdigit():
            self.result_label.config(text="Ошибка: Введите корректную сумму", fg="red")
            return

        # Обновление текста результата
        result_text = f"Операция: {operation_type}\nСумма: {amount} Br"
        self.result_label.config(text=result_text, fg="green")
