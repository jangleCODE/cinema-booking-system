from cinema import Cinema
from booking_services import BookingService
from cli import CinemaCLI
from logger_config import setup_logger
import logging

def main():
    setup_logger()
    while True:
        try:
            config = input("Please define movie title and seating map in [Title] [Row] [SeatsPerRow] format:\n> ").strip().rsplit(' ', 2)
            if len(config) == 3 and config[1].isdigit() and config[2].isdigit():
                title = config[0] # gets the name (can be multiple words)
                rows = int(config[1]) # converted to integers
                seats_per_row = int(config[2]) # converted to integers
                if 1 <= rows <= 26 and 1 <= seats_per_row <= 50:
                    break
                print("Max 26 rows and 50 seats per row allowed.")
            else:
                print("Invalid format. Try again.")
        except ValueError as ve:
            logging.warning(f"Input error: {ve}")
            print(ve)

    cinema = Cinema(title, rows, seats_per_row)
    service = BookingService(cinema)
    cli = CinemaCLI(service)
    cli.start()

if __name__ == "__main__":
    main()
