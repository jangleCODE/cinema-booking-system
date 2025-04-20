from gic_app.cinema import Cinema
from gic_app.booking_services import BookingService
from gic_app.cli import CinemaCLI

def test_end_to_end_booking(monkeypatch, capsys):
    cinema = Cinema("Test Movie", 2, 2)
    service = BookingService(cinema)
    cli = CinemaCLI(service)

    inputs = iter([
        "1",        # Choose to book tickets
        "2",        # Number of tickets
        "",         # Accept default seating
        "3"         # Exit
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    cli.start()
    captured = capsys.readouterr()
    assert "Booking id:" in captured.out
    assert "confirmed" in captured.out
