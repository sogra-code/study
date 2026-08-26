"""Точка входа командной строки."""

from __future__ import annotations

import argparse
import sys

from hello_app.greeter import greet


def build_parser() -> argparse.ArgumentParser:
    """Собирает аргументы командной строки."""
    parser = argparse.ArgumentParser(
        prog="hello-app",
        description="Учебное Python-приложение для сборки в Jenkins.",
    )
    parser.add_argument("--name", default="world", help="Кого поприветствовать")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Точка входа: печатает приветствие и возвращает код возврата."""
    args = build_parser().parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
