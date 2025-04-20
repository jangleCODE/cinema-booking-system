import pytest
from gic_app.cinema import Cinema
from gic_app.booking_services import BookingService

def test_booking_service_init():
    cinema = Cinema("Matrix", 3, 3)
    service = BookingService(cinema)
    assert service.cinema.title == "Matrix"

def test_generate_booking_id():
    cinema = Cinema("Matrix", 3, 3)
    service = BookingService(cinema)
    assert service.generate_booking_id() == "GIC0001"
    assert service.generate_booking_id() == "GIC0002"

def test_find_best_seats():
    cinema = Cinema("Matrix", 3, 3)
    service = BookingService(cinema)
    best = service.find_best_seats(3)
    assert len(best) == 3
    for r, c in best:
        assert service.cinema.seating[r][c] == '.'

def test_parse_manual_position_valid():
    cinema = Cinema("Matrix", 3, 3)
    service = BookingService(cinema)
    result = service.parse_manual_position("A01", 2)
    assert result == [(0, 0), (0, 1)]

def test_parse_manual_position_invalid_format():
    cinema = Cinema("Matrix", 3, 3)
    service = BookingService(cinema)
    result = service.parse_manual_position("Z100", 2)
    assert result == []

def test_parse_manual_position_unavailable_seat():
    cinema = Cinema("Matrix", 3, 3)
    service = BookingService(cinema)
    service.cinema.seating[0][0] = '#'
    result = service.parse_manual_position("A01", 2)
    assert result == []

def test_reserve_seats():
    cinema = Cinema("Frozen", 5, 5)
    service = BookingService(cinema)
    booking_id = service.generate_booking_id()
    seats = [(0, 0), (0, 1)]
    service.reserve_seats(booking_id, seats)
    assert service.cinema.seating[0][0] == '#'
    assert service.cinema.seating[0][1] == '#'
    assert service.get_booking(booking_id) == seats
    assert service.cinema.available_seats == 23  # 25 - 2

def test_get_booking_case_insensitive():
    cinema = Cinema("Matrix", 3, 3)
    service = BookingService(cinema)
    booking_id = service.generate_booking_id()
    seats = [(1, 0), (1, 1)]
    service.reserve_seats(booking_id, seats)
    assert service.get_booking(booking_id.lower()) == seats