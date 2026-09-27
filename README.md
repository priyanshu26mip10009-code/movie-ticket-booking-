# 🎬 Movie Ticket Booking System

A simple **Movie Ticket Booking System** developed using **Python**.
This is a console-based application that allows users to view movies, select shows, book seats, search bookings, cancel tickets, and manage bookings.

## 📌 Project Description

The Movie Ticket Booking System is designed to make the process of booking movie tickets simple and convenient.

The system provides different options for customers and administrators. Customers can select a movie, choose a show timing, select available seats, enter their details, and complete a booking.

An administrator can add movies, view bookings, and check the total revenue.

## ✨ Features

### 👤 Customer Features

* Display available movies
* Search for movies
* View movie details
* View show timings
* Select seats
* Check seat availability
* Book movie tickets
* Enter customer details
* Calculate ticket price
* Calculate 5% tax
* Select payment method
* Generate booking ID
* Search booking
* Cancel booking
* View booking history
* View personal bookings

### 🔐 Admin Features

* Admin login
* Add new movies
* View all bookings
* View total revenue
* Display movies
* Logout from admin account

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Type:** Console-based application
* **Libraries:**

  * `random`
  * `datetime`

No external libraries are required.

## 💻 Requirements

To run this project, you need:

* Python 3.x
* Any Python IDE or code editor

Examples:

* IDLE
* VS Code
* PyCharm
* Jupyter-compatible environment

## 🚀 How to Run

### Step 1: Install Python

Install Python 3.x on your computer.

### Step 2: Save the Program

Save the Python program as:

```text
movie_ticket_booking.py
```

### Step 3: Run the Program

Open a terminal in the project folder and run:

```bash
python movie_ticket_booking.py
```

The main menu will appear on the screen.

## 📋 Main Menu

The program provides the following options:

```text
1. Display Movies
2. Search Movie
3. Book Ticket
4. Search Booking
5. Cancel Booking
6. Booking History
7. My Bookings
8. Admin Login
9. Exit
```

## 🎟️ Booking Process

The basic booking process is:

```text
Start
   ↓
Display Movies
   ↓
Select Movie
   ↓
Select Show
   ↓
Select Available Seats
   ↓
Enter Customer Details
   ↓
Calculate Bill
   ↓
Select Payment Method
   ↓
Confirm Booking
   ↓
Generate Booking ID
   ↓
Save Booking
   ↓
Display Confirmation
```

## 💺 Seat Layout

The system provides 64 seats arranged in 8 rows.

```text
[A1] [A2] [A3] [A4] [A5] [A6] [A7] [A8]
[B1] [B2] [B3] [B4] [B5] [B6] [B7] [B8]
[C1] [C2] [C3] [C4] [C5] [C6] [C7] [C8]
[D1] [D2] [D3] [D4] [D5] [D6] [D7] [D8]
[E1] [E2] [E3] [E4] [E5] [E6] [E7] [E8]
[F1] [F2] [F3] [F4] [F5] [F6] [F7] [F8]
[G1] [G2] [G3] [G4] [G5] [G6] [G7] [G8]
[H1] [H2] [H3] [H4] [H5] [H6] [H7] [H8]
```

`XX` represents a booked seat.

## 💰 Bill Calculation

The system calculates the total ticket amount using:

```text
Ticket Price = Movie Price × Number of Seats

Tax = Ticket Price × 5%

Total Amount = Ticket Price + Tax
```

## 💳 Payment Methods

The system provides three payment options:

1. UPI
2. Card
3. Cash

## 🔑 Admin Login

The default administrator credentials are:

```text
Username: admin
Password: 1234
```

The administrator can:

* Add movies
* View all bookings
* Check revenue
* View movies

## 📂 Project Structure

```text
Movie-Ticket-Booking/
│
├── movie_ticket_booking.py
└── README.md
```

## 🧠 Python Concepts Used

This project demonstrates several basic Python concepts:

* Variables
* Lists
* Dictionaries
* Functions
* `if-else` statements
* `for` loops
* `while` loops
* Exception handling
* User input
* String operations
* Basic calculations
* Date and time
* Random number generation

## ⚠️ Limitations

This is a basic console-based project.

* Booking data is stored only while the program is running.
* Data is not stored in a database.
* Payment is simulated.
* There is no graphical user interface.
* There is no real online payment system.
* Multiple users cannot use the system simultaneously.

## 🔮 Future Improvements

The project can be improved by adding:

* Database support using MySQL or SQLite
* Graphical User Interface using Tkinter
* Online payment integration
* User registration and login
* Email/SMS ticket confirmation
* Movie posters
* Multiple theatres
* Different seat categories
* Automatic ticket printing
* Persistent booking history

## 👨‍💻 Project Purpose

This project is created for educational purposes to demonstrate the implementation of a basic **Movie Ticket Booking System using Python**.

## 📜 License

This project is free to use for educational and learning purposes.

---

### 🎬 Thank You

Thank you for using the **Movie Ticket Booking System**!
