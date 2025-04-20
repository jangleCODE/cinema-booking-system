class CinemaCLI:
    def __init__(self, service):
        self.service = service

    def start(self):
        while True:
            print("\nWelcome to GIC Cinemas")
            print(f"[1] Book tickets for {self.service.cinema.title} ({self.service.cinema.available_seats} seats available)")
            print("[2] Check bookings")
            print("[3] Exit")
            print("Please enter your selection:")
            choice = input("> ").strip()

            if choice == '1':
                self.book_tickets()
            elif choice == '2':
                self.check_booking()
            elif choice == '3':
                print("\nThank you for using GIC Cinemas system. Bye!")
                break
            else:
                print("Invalid selection.")

    def display_seating(self, highlight=None):
        print("\n          S C R E E N")
        print("-" * (self.service.cinema.seats_per_row * 2 + 6)) # Divider line
        for i in range(self.service.cinema.rows - 1, -1, -1):
            row_label = chr(ord('A') + i)
            print(row_label, end=' ')
            for j in range(self.service.cinema.seats_per_row): # Print each seat in the row
                seat = 'o' if highlight and (i, j) in highlight else self.service.cinema.seating[i][j]
                print(seat, end='  ')
            print()
        print("  ", end='')
        for i in range(1, self.service.cinema.seats_per_row + 1):
            print(f"{i:2}", end=' ')
        print('\n')

    def book_tickets(self):
        while True:
            count = input("\nEnter number of tickets to book, or enter blank to go back to main menu:\n> ").strip()
            if not count: # Exit if input is blank
                return
            if not count.isdigit(): # If the input isn’t all digits (like "abc" or "1a"), skip and ask again
                continue
            num = int(count)
            if num > self.service.cinema.available_seats:
                print(f"\nSorry, there are only {self.service.cinema.available_seats} seats available.")
                continue

            booking_id = self.service.generate_booking_id()
            seats = self.service.find_best_seats(num)
            print(f"\nSuccessfully reserved {num} {self.service.cinema.title} tickets.")
            print(f"Booking id: {booking_id}\nSelected seats:")
            self.display_seating(highlight=seats)

            while True:
                pos = input("Enter blank to accept seat selection, or enter new seating position (e.g. B03):\n> ").strip()
                if not pos:
                    break
                new_seats = self.service.parse_manual_position(pos, num)
                if new_seats:
                    seats = new_seats
                    print(f"\nBooking id: {booking_id}\nSelected seats:")
                    self.display_seating(highlight=seats)
                else:
                    print("Invalid or unavailable seat selection.")

            self.service.reserve_seats(booking_id, seats)
            print(f"\nBooking id: {booking_id} confirmed.")
            break

    def check_booking(self):
        while True:
            bid = input("\nEnter booking id, or enter blank to go back to main menu:\n> ").strip()
            if not bid: # Return if input is blank
                return
            seats = self.service.get_booking(bid)
            if seats:
                print(f"\nBooking id: {bid}\nSelected seats:")
                self.display_seating(highlight=seats)
            else:
                print("Booking ID not found.")

    # For unit testing purposes
    def book_tickets_manual(self, ticket_count, manual_pos=None):
        if ticket_count > self.service.cinema.available_seats:
            return "Not enough seats"

        booking_id = self.service.generate_booking_id()
        seats = self.service.find_best_seats(ticket_count)

        if manual_pos:
            new_seats = self.service.parse_manual_position(manual_pos, ticket_count)
            if new_seats:
                seats = new_seats

        self.service.reserve_seats(booking_id, seats)
        return {"booking_id": booking_id, "seats": seats}
    
    def check_booking_by_id(self, booking_id):
        seats = self.service.get_booking(booking_id)
        return seats
