import pytest
from gic_app.cinema import Cinema

def test_initialize_cinema():
    cinema = Cinema("Avengers", 5, 10)
    assert cinema.total_seats == 50
    assert cinema.available_seats == 50

def test_get_available_seats():
    cinema = Cinema("Avengers", 5, 5)
    seats = cinema.get_available_seats(3)
    assert all(isinstance(seat, tuple) and len(seat) == 2 for seat in seats)
    assert all(cinema.seats[r][c] == '.' for r, c in seats)
    assert len(seats) > 0  # Just check we got some valid results

def test_parse_position_valid():
    cinema = Cinema("Avengers", 5, 5)
    pos = cinema.parse_position("A1", 2)
    assert pos == (0, 0)

def test_parse_position_invalid():
    cinema = Cinema("Avengers", 5, 5)
    pos = cinema.parse_position("Z99", 2)
    assert pos == []