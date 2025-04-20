class Cinema:
    def __init__(self, title, rows, seats_per_row):
        self.title = title
        self.rows = rows # Stores how many row the cinema has
        self.seats = [['.' for _ in range(seats_per_row)] for _ in range(rows)] # Creates a 2D list of seats using . to represent empty seats
        self.seats_per_row = seats_per_row # Stores how many seats per row the cinema has
        self.total_seats = rows * seats_per_row # Calculates and stores the total seat count
        self.available_seats = self.total_seats # Calculates and stores the available seat count
        self.seating = [['.' for _ in range(seats_per_row)] for _ in range(rows)] # Used for displaying with highlights
        self.booked_seats = set() # Keeps track of which seats are booked using a set of coordinate tuples

    def get_available_seats(self, group_size):
        available = []
        
        for r_idx, row in enumerate(self.seats): # Loops through each row in the seating chart
            consecutive_seats = 0
            for s_idx, seat in enumerate(row):
                if seat == '.':  # '.' means the seat is available
                    consecutive_seats += 1
                    if consecutive_seats == group_size:
                        # Add the starting positions of the group of available seats
                        available.append((r_idx, s_idx - group_size + 1))
                        consecutive_seats -= 1  # keep checking for overlapping groups
                else:
                    consecutive_seats = 0

        return available
    
    # Convert a seat label like "B03" into a tuple like (1, 2) that can be used to access the internal 2D seating array
    def parse_position(self, start_label, group_size):
        row_label = start_label[0]  # 'A', 'B', etc.
        seat_label = int(start_label[1:])  # '1', '2', etc.
        
        row_idx = ord(row_label) - ord('A')
        # Validate row and seat
        if row_idx < 0 or row_idx >= self.rows:
            return [] # Invalid row

        seat_idx = seat_label - 1  # Convert to 0-indexed
        if seat_idx < 0 or seat_idx >= self.seats_per_row:
            return []  # Invalid seat
        
        return (row_idx, seat_idx)