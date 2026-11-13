import pytest
from hypothesis import example, given, settings, strategies as st

from traffic_fine import parse_ticket_id, speed_excess, total_fines


INVALID_TYPES = st.none() | st.booleans() | st.integers() | st.binary()
INVALID_TEXT = st.text(alphabet="abcXYZ ", max_size=30)
AMOUNTS = st.integers(min_value=0, max_value=20000)


@settings(derandomize=True)
@given(INVALID_TYPES | INVALID_TEXT | st.sampled_from(["-2024-1", "TF-2024-"]))
def test_parse_ticket_id_rejects_invalid_input(value):
    with pytest.raises(ValueError):
        parse_ticket_id(value)


@settings(derandomize=True)
@given(
    INVALID_TYPES | INVALID_TEXT
    | st.integers(min_value=-20000, max_value=-1).map(str)
    | st.sampled_from(["1,,2", "1,", "12000,-1"])
)
def test_total_fines_rejects_invalid_input(value):
    with pytest.raises(ValueError):
        total_fines(value)


@settings(derandomize=True)
@given(
    INVALID_TYPES | INVALID_TEXT
    | st.integers(min_value=0).map(lambda speed: f"{speed}/0")
    | st.sampled_from(["-1/60", "1/-60", "1/2/3"])
)
def test_speed_excess_rejects_invalid_input(value):
    with pytest.raises(ValueError):
        speed_excess(value)


@settings(derandomize=True)
@given(st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1, max_size=8),
       st.integers(min_value=1, max_value=9999), AMOUNTS)
@example("tf", 2024, 456)
def test_parse_ticket_id_returns_normalized_parts(prefix, year, serial):
    assert parse_ticket_id(f"{prefix}-{year:04d}-{serial:06d}") == (
        prefix.upper(), year, serial
    )


@settings(derandomize=True)
@given(st.lists(AMOUNTS, min_size=1, max_size=25))
@example([9999, 1])
@example([9999, 2])
def test_total_fines_returns_capped_sum(amounts):
    assert total_fines(", ".join(map(str, amounts))) == min(sum(amounts), 10000)


@settings(derandomize=True)
@given(st.integers(min_value=0, max_value=500),
       st.integers(min_value=1, max_value=500))
@example(72, 60)
@example(59, 60)
@example(60, 60)
def test_speed_excess_returns_floor_percentage(speed, limit):
    result = speed_excess(f"{speed}/{limit}")
    difference = 100 * (speed - limit)
    assert result * limit <= difference < (result + 1) * limit
