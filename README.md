# 🎬 GIC Cinema Booking Application

A command-line cinema booking application built with Python. This app allows users to search for available movies, book tickets, and manage reservations.

The system is designed using two main classes:

1. Cinema: Manages seating, seat availability, and basic utilities.
2. BookingService: Handles the business logic for auto/manual bookings and manages bookings per group.
3. CLI: The user interface of the application

# 🎨 DESIGN ASSUMPTIONS

- Seats are represented using a 2D list (`seats` or `seating`) where `'.'` means available, `'X'` or `'#'` means booked.
- Booking IDs are generated in the format `GIC0001`, `GIC0002`, etc.
- Auto-assignment starts from the top-left and prefers centering the group if possible.
- Manual booking expects a seat label like `A01`, `B02`, etc.
- The application is **console-based** and mainly meant to be run/tested using **unit tests**.

# ⚙️ REQUIREMENTS & ENVIRONMENT

- OS: Windows or Linux (any OS with Python support)
- Python Version: 3.8 or higher
- Recommended Virtual Environment: `venv` or `virtualenv`


# ▶️ How to Run the Application
```bash
### 1. Clone the Repository
git clone https://github.com/jangleCODE/cinema-booking-system.git
cd gic_app

### 2. Set Up the Virtual Environment
python -m venv venv
### 2.1 Activate the Virtual Environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Application
python main.py

```
# 🧪 Running the Tests

```bash
# Run All Tests
pytest tests/
# Run a Specific Test File
pytest tests/test_booking_service.py

```

👤 Author
Created by Jan Ng