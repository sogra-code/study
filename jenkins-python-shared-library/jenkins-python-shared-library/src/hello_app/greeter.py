"""Приветствия и простые текстовые утилиты."""

from __future__ import annotations


def greet(name: str = "world") -> str:
    """Возвращает приветствие для указанного имени.

    Пустое имя (или строка из пробелов) заменяется на "world".
    """
    name = name.strip()
    if not name:
        name = "world"
    return f"Hello, {name}!"


def word_count(text: str) -> int:
    """Подсчитывает количество слов в тексте."""
    return len(text.split())
