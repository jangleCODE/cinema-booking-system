import re
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BookingService:
    def __init__(self, cinema):
        self.cinema = cinema
        self.bookings = {}
        self.booking_counter = 1
    
    def generate_booking_id(self):
        bid = f"GIC{self.booking_counter:04}"
        self.booking_counter += 1
        print(f"___Generated booking ID: {bid}")
        return bid

    def find_best_seats(self, count):
        highlight = []
        for i in range(self.cinema.rows):
            # Calculate center-first seat order
            mid = self.cinema.seats_per_row // 2
            indices = sorted(range(self.cinema.seats_per_row), key=lambda x: abs(x - mid))
            # Check availability in that row
            for j in indices:
                if self.cinema.seating[i][j] == '.':
                    highlight.append((i, j))
                    if len(highlight) == count:
                        return highlight
        return []

    def parse_manual_position(self, pos, count):
        match = re.fullmatch(r"([A-Z])(\d{1,2})", pos.upper())
        if not match:
            return []
        row = ord(match.group(1)) - ord('A')
        col = int(match.group(2)) - 1

        highlight = []
        r, c = row, col

        while r < self.cinema.rows and len(highlight) < count:
            while c < self.cinema.seats_per_row and len(highlight) < count:
                if self.cinema.seating[r][c] != '.':
                    return []
                highlight.append((r, c))
                c += 1
            mid = self.cinema.seats_per_row // 2
            c = mid - (count // 2)
            if c < 0: c = 0
            r += 1
        
        if not (0 <= row < self.cinema.rows) or not (0 <= col < self.cinema.seats_per_row):
            print("Invalid manual seat reference.")
            return []

        return highlight if len(highlight) == count else []

    def reserve_seats(self, booking_id, seats):
        try:
            for r, c in seats:
                self.cinema.seating[r][c] = '#'
            self.bookings[booking_id] = seats
            self.cinema.available_seats -= len(seats)
        except Exception as e:
            logger.error(f"Failed to reserve seats: {e}")

    def get_booking(self, booking_id):
        return self.bookings.get(booking_id.upper())