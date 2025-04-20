import pytest
from gic_app.cinema import Cinema
from gic_app.booking_services import BookingService
from gic_app.cli import CinemaCLI

def test_display_seating(monkeypatch, capsys):
    cinema = Cinema("Garfield", 2, 2)
    service = BookingService(cinema)
    cli = CinemaCLI(service)

    cli.display_seating()
    captured = capsys.readouterr()
    assert "         S C R E E N" in captured.out
    assert "." in captured.out

@pytest.fixture
def cli():
    cinema = Cinema("Garfield", 3, 5)
    service = BookingService(cinema)
    return CinemaCLI(service)

def test_book_tickets_manual(cli):
    result = cli.book_tickets_manual(2)
    assert isinstance(result, dict)
    assert result["booking_id"].startswith("GIC")
    assert len(result["seats"]) == 2

def test_book_tickets_with_manual_position(cli):
    result = cli.book_tickets_manual(2, manual_pos="A01")
    assert isinstance(result, dict)
    assert result["seats"] == [(0, 0), (0, 1)]

def test_check_booking_by_id(cli):
    booking = cli.book_tickets_manual(1)
    found = cli.check_booking_by_id(booking["booking_id"])
    assert found == booking["seats"]

def test_check_invalid_booking_id(cli):
    result = cli.check_booking_by_id("INVALID")
    assert result is None