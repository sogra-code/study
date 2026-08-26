"""Простая статистика по списку чисел."""

from __future__ import annotations

from statistics import fmean


def summarize(values: list[float]) -> dict[str, int | float]:
    """Возвращает count, sum, mean, min, max для списка чисел.

    Raises:
        ValueError: если список пуст.
    """
    if not values:
        raise ValueError("values must not be empty")
    return {
        "count": len(values),
        "sum": sum(values),
        "mean": fmean(values),
        "min": min(values),
        "max": max(values),
    }
