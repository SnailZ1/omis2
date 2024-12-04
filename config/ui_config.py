WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

# Настройки для начального окна
START_WINDOW = {
    "title": "Приложение",
    "logo_path": "asset/logo.png",  # Путь к логотипу
}

# Настройки для окна авторизации
AUTH_WINDOW = {
    "title": "Авторизация",
}

# Настройки для окна регистрации
REGISTER_WINDOW = {
    "title": "Регистрация",
}

# Настройки для центрации окон
WINDOW_POSITION = {
    "center": True,  # Все окна должны быть по центру экрана
}

def center_window(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_offset = (screen_width - width) // 2
    y_offset = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
