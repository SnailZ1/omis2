import tkinter as tk
from view.account_view import AccountView
from view.payment_view import PaymentView
from view.history_view import HistoryView
from view.profile_view import ProfileView

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Главное окно")
        self.setup_window()

        # Разделение на левую панель (для навигации) и центральную область
        self.left_panel = tk.Frame(self.root, width=200, bg="#f0f0f0", height=500)
        self.left_panel.pack(side="left", fill="y")

        self.center_panel = tk.Frame(self.root, width=800, bg="#ffffff", height=500)
        self.center_panel.pack(side="left", expand=True, fill="both")

        # Кнопки на левой панели
        self.current_button = tk.Button(self.left_panel, text="Главная", command=self.show_current, relief="flat")
        self.current_button.pack(pady=10, fill="x")

        self.payment_button = tk.Button(self.left_panel, text="Платежи", command=self.show_payments, relief="flat")
        self.payment_button.pack(pady=10, fill="x")

        self.history_button = tk.Button(self.left_panel, text="История платежей", command=self.show_history, relief="flat")
        self.history_button.pack(pady=10, fill="x")

        self.profile_button = tk.Button(self.left_panel, text="Личный кабинет", command=self.show_profile, relief="flat")
        self.profile_button.pack(pady=10, fill="x")

        # Инициализация активной кнопки
        self.active_button = None

        # Отображаем первое окно по умолчанию (например, Текущее)
        self.show_current()

    def setup_window(self):
        """Настройка главного окна, установка размеров и центрирование"""
        window_width = 1024
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.resizable(False, False)

    def update_active_button(self, new_button):
        """Обновляем активную кнопку и её стиль"""
        # Сброс старой активной кнопки
        if self.active_button:
            self.active_button.config(bg="#f0f0f0", fg="black")

        # Устанавливаем новую активную кнопку
        new_button.config(bg="#0056b3", fg="white")
        self.active_button = new_button

    def show_current(self):
        """Отображение содержимого для текущих счетов"""
        self.update_active_button(self.current_button)  # Обновляем активную кнопку
        for widget in self.center_panel.winfo_children():
            widget.destroy()  # Удаляем старое содержимое
        current_view = AccountView(self.center_panel)
        current_view.pack(fill="both", expand=True)

    def show_payments(self):
        """Отображение содержимого для платежей"""
        self.update_active_button(self.payment_button)  # Обновляем активную кнопку
        for widget in self.center_panel.winfo_children():
            widget.destroy()
        payment_view = PaymentView(self.center_panel)
        payment_view.pack(fill="both", expand=True)

    def show_history(self):
        """Отображение содержимого для истории платежей"""
        self.update_active_button(self.history_button)  # Обновляем активную кнопку
        for widget in self.center_panel.winfo_children():
            widget.destroy()
        history_view = HistoryView(self.center_panel)
        history_view.pack(fill="both", expand=True)

    def show_profile(self):
        """Отображение содержимого для личного кабинета"""
        self.update_active_button(self.profile_button)  # Обновляем активную кнопку
        for widget in self.center_panel.winfo_children():
            widget.destroy()
        profile_view = ProfileView(self.center_panel)
        profile_view.pack(fill="both", expand=True)
