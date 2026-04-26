quotes = [
    {"text": "Будь тем изменением, которое ты хочешь видеть в мире.", "author": "Махатма Ганди", "theme": "Изменения"},
    {"text": "Счастье — это не что иное, как хорошее здоровье и плохая память.", "author": "Альберт Эйнштейн", "theme": "Счастье"},
    {"text": "Жизнь — это то, что происходит, пока вы строите другие планы.", "author": "Джон Леннон", "theme": "Жизнь"},
    {"text": "Только тот, кто рискует зайти слишком далеко, может узнать, насколько далеко он может зайти.", "author": "Т. С. Элиот", "theme": "Риск"},
]

import random

def generate_quote():
    return random.choice(quotes)

history = []

def display_history():
    for quote in history:
        print(f"{quote['text']} - {quote['author']} ({quote['theme']})")


def filter_by_author(author):
    return [quote for quote in history if quote['author'] == author]

def filter_by_theme(theme):
    return [quote for quote in history if quote['theme'] == theme]

import json

def save_history(filename='history.json'):
    with open(filename, 'w') as f:
        json.dump(history, f)

def load_history(filename='history.json'):
    global history
    with open(filename, 'r') as f:
        history = json.load(f)


def add_quote(text, author, theme):
    if not text or not author or not theme:
        print("Ошибка: Пустые строки недопустимы.")
        return
    new_quote = {"text": text, "author": author, "theme": theme}
    history.append(new_quote)
