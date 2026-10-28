"""Data checks used by the teaching example."""

from __future__ import annotations

import math
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True)
class Issue:
    kind: str
    message: str
    row_number: int | None = None


def in_range(value: float, minimum: float, maximum: float) -> bool:
    """Return True when value is within the inclusive range."""
    return minimum <= value <= maximum


def find_missing(rows: Iterable[dict[str, str]], column: str) -> list[Issue]:
    """Find rows where a required column is blank."""
    issues: list[Issue] = []
    for row_number, row in enumerate(rows, start=2):
        if row.get(column, "").strip() == "":
            issues.append(Issue("missing", f"Missing value in {column}", row_number))
    return issues


def find_duplicates(rows: Iterable[dict[str, str]], key: str) -> list[Issue]:
    """Find repeated values in a column."""
    seen: dict[str, int] = {}
    issues: list[Issue] = []
    for row_number, row in enumerate(rows, start=2):
        value = row.get(key, "")
        if value in seen:
            issues.append(Issue("duplicate", f"Duplicate {key}: {value}", row_number))
        else:
            seen[value] = row_number
    return issues


def check_numeric_range(
    rows: Iterable[dict[str, str]],
    column: str,
    minimum: float,
    maximum: float,
) -> list[Issue]:
    """Find numeric values outside an inclusive range."""
    issues: list[Issue] = []
    for row_number, row in enumerate(rows, start=2):
        raw = row.get(column, "").strip()
        if raw == "":
            continue
        try:
            value = float(raw)
        except ValueError:
            issues.append(
                Issue("invalid", f"Non-numeric value in {column}: {raw}", row_number)
            )
            continue
        if not math.isfinite(value):
            issues.append(
                Issue("invalid", f"Non-finite value in {column}: {raw}", row_number)
            )
            continue
        if not in_range(value, minimum, maximum):
            issues.append(
                Issue(
                    "range",
                    f"{column}={value} is outside [{minimum}, {maximum}]",
                    row_number,
                )
            )
    return issues
