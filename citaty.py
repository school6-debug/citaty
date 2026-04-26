import tkinter as tk
from tkinter import messagebox, Listbox, StringVar, OptionMenu
import json
import random

class QuoteGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")

        # Предопределённые цитаты
        self.quotes = [
            {"text": "Будь собой; все остальные роли уже заняты.", "author": "Оскар Уайльд", "theme": "Саморазвитие"},
            {"text": "Жизнь — это то, что происходит, пока вы строите другие планы.", "author": "Джон Леннон", "theme": "Жизнь"},
            {"text": "Счастье — это не что иное, как хорошее здоровье и плохая память.", "author": "Альберт Эйнштейн", "theme": "Счастье"},
            {"text": "Не бойтесь совершенства — вам его не достичь.", "author": "Сальвадор Дали", "theme": "Искусство"},
            {"text": "Чем больше я работаю, тем больше мне везёт.", "author": "Томас Эдисон", "theme": "Успех"}
        ]

        self.history = []

        # Кнопка для генерации цитаты
        self.generate_button = tk.Button(root, text="Сгенерировать цитату", command=self.generate_quote)
        self.generate_button.pack(pady=10)

        # Поле для отображения цитаты
        self.quote_label = tk.Label(root, text="", wraplength=300, justify="center")
        self.quote_label.pack(pady=10)

        # Таблица истории
        self.history_label = tk.Label(root, text="История цитат:")
        self.history_label.pack(pady=5)

        self.history_list = Listbox(root, width=50)
        self.history_list.pack(pady=5)

        # Фильтрация
        self.filter_label = tk.Label(root, text="Фильтрация по автору:")
        self.filter_label.pack(pady=5)

        self.filter_author_var = StringVar(root)
        self.filter_author_var.set("Все")  # Значение по умолчанию
        self.author_menu = OptionMenu(root, self.filter_author_var, "Все", *set(quote["author"] for quote in self.quotes))
        self.author_menu.pack(pady=5)

        self.filter_button = tk.Button(root, text="Фильтровать", command=self.filter_quotes)
        self.filter_button.pack(pady=5)

        # Загрузка истории из файла
        self.load_history()

    def generate_quote(self):
        quote = random.choice(self.quotes)
        self.quote_label.config(text=f'"{quote["text"]}"\n— {quote["author"]} ({quote["theme"]})')
        
        # Сохранение в историю
        self.history.append(quote)
        self.update_history_display()
        self.save_history()

    def update_history_display(self):
        self.history_list.delete(0, tk.END)
        
        for quote in self.history:
            display_text = f'"{quote["text"]}" — {quote["author"]} ({quote["theme"]})'
            self.history_list.insert(tk.END, display_text)

    def filter_quotes(self):
        selected_author = self.filter_author_var.get()
        
        if selected_author == "Все":
            filtered_quotes = self.history
        else:
            filtered_quotes = [quote for quote in self.history if quote["author"] == selected_author]

        self.history_list.delete(0, tk.END)
        
        for quote in filtered_quotes:
            display_text = f'"{quote["text"]}" — {quote["author"]} ({quote["theme"]})'
            self.history_list.insert(tk.END, display_text)

    def load_history(self, filename='history.json'):
        try:
            with open(filename, 'r') as f:
                self.history = json.load(f)
                self.update_history_display()
        except FileNotFoundError:
            pass
    def save_history(self, filename='history.json'):
        with open(filename, 'w') as f:
            json.dump(self.history, f)

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = QuoteGeneratorApp(root)
    root.mainloop()
