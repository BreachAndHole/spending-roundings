from typing import NamedTuple


class RoundingBoundary(NamedTuple):
    start: int
    end: int
    ceiling: int


BOUNDARIES = [
    RoundingBoundary(start=0, end=50, ceiling=10),
    RoundingBoundary(start=50, end=300, ceiling=50),
    RoundingBoundary(start=300, end=2_000, ceiling=100),
    RoundingBoundary(start=2_000, end=10_000, ceiling=500),
    RoundingBoundary(start=10_000, end=1_000_000, ceiling=1_000)
]


def _calculate_rounding(amount: float, boundary: RoundingBoundary) -> float:
    rounding_amount = round(boundary.ceiling - amount % boundary.ceiling, 2)
    return rounding_amount


def calculate_all_roundings(spending: list[float]) -> list[float]:
    result = []
    for spend in spending:
        for j, boundary in enumerate(BOUNDARIES):
            if boundary.start <= spend < boundary.end:
                amount = _calculate_rounding(spend, boundary)
                result.append(amount)
                break
    return result
