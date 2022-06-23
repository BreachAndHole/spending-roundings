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