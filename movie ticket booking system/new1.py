# ============================================================
#              MOVIE TICKET BOOKING SYSTEM
# ============================================================

import random
import datetime


# ----------------------- MOVIES -----------------------------

movies = [
    {
        "id": 1,
        "name": "Avengers End Game",
        "language": "English",
        "genre": "Action",
        "price": 250
    },
    {
        "id": 2,
        "name": "sinners",
        "language": "english",
        "genre": "horror",
        "price": 180
    },
    {
        "id": 3,
        "name": "ford v ferrari",
        "language": "english",
        "genre": "Sports",
        "price": 200
    },
    {
        "id": 4,
        "name": "pacific rim",
        "language": "english",
        "genre": "Action",
        "price": 220
    }
]


shows = {
    1: ["10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM"],
    2: ["9:00 AM", "1:00 PM", "5:00 PM", "8:00 PM"],
    3: ["10:30 AM", "2:30 PM", "6:30 PM", "9:30 PM"],
    4: ["9:30 AM", "1:30 PM", "5:30 PM", "8:30 PM"]
}


bookings = []


# ----------------------- BASIC FUNCTIONS --------------------

def line():
    print("=" * 55)


def pause():
    input("\nPress Enter to continue...")


def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None


def booking_id():
    return "MOV" + str(random.randint(10000, 99999))


# ----------------------- DISPLAY MOVIES ---------------------

def display_movies():
    line()
    print("                    MOVIES")
    line()

    for movie in movies:
        print(
            movie["id"],
            "-",
            movie["name"],
            "|",
            movie["language"],
            "|",
            movie["genre"],
            "| ₹",
            movie["price"]
        )

    line()


# ----------------------- SHOWS ------------------------------

def select_movie():
    display_movies()

    while True:
        try:
            choice = int(input("Enter Movie ID: "))
            movie = get_movie(choice)

            if movie:
                return movie

            print("Movie not found.")

        except ValueError:
            print("Enter a valid number.")


def select_show(movie):
    line()
    print("SHOW TIMINGS")
    line()

    show_list = shows.get(movie["id"], [])

    for i, show in enumerate(show_list, 1):
        print(i, ".", show)

    while True:
        try:
            choice = int(input("Select show: "))

            if 1 <= choice <= len(show_list):
                return show_list[choice - 1]

            print("Invalid choice.")

        except ValueError:
            print("Enter a number.")


# ----------------------- SEATS ------------------------------

def booked_seats(movie_id, show):
    seats = []

    for booking in bookings:
        if (
            booking["movie_id"] == movie_id
            and booking["show"] == show
            and booking["status"] == "Confirmed"
        ):
            seats += booking["seats"]

    return seats


def display_seats(movie_id, show):
    booked = booked_seats(movie_id, show)

    line()
    print("                    SEATS")
    line()

    for row in "ABCDEFGH":
        for number in range(1, 9):

            seat = row + str(number)

            if seat in booked:
                print("[XX]", end=" ")

            else:
                print("[" + seat + "]", end=" ")

        print()

    line()
    print("XX = Booked")


def select_seats(movie, show):

    display_seats(movie["id"], show)

    booked = booked_seats(
        movie["id"],
        show
    )

    while True:
        try:
            count = int(
                input("Number of seats: ")
            )

            if count > 0:
                break

            print("Enter a positive number.")

        except ValueError:
            print("Enter a number.")

    selected = []

    for i in range(count):

        while True:

            seat = input(
                "Enter seat "
                + str(i + 1)
                + ": "
            ).upper()

            if (
                len(seat) >= 2
                and seat[0] in "ABCDEFGH"
                and seat[1:].isdigit()
            ):

                number = int(seat[1:])

                if 1 <= number <= 8:

                    if seat not in booked and seat not in selected:
                        selected.append(seat)
                        break

            print("Invalid or unavailable seat.")

    return selected


# ----------------------- BOOKING ----------------------------

def book_ticket():

    print()
    line()
    print("                 BOOK TICKET")
    line()

    movie = select_movie()

    show = select_show(movie)

    seats = select_seats(
        movie,
        show
    )

    print()
    line()
    print("CUSTOMER DETAILS")
    line()

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    ticket_price = movie["price"] * len(seats)

    tax = ticket_price * 0.05

    total = ticket_price + tax

    line()
    print("BILL")
    line()

    print("Movie       :", movie["name"])
    print("Show        :", show)
    print("Seats       :", ", ".join(seats))
    print("Ticket Price: ₹", ticket_price)
    print("Tax         : ₹", round(tax, 2))
    print("Total       : ₹", round(total, 2))

    line()

    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    payment_choice = input(
        "Payment method: "
    )

    payment = {
        "1": "UPI",
        "2": "Card",
        "3": "Cash"
    }.get(payment_choice)

    if payment is None:
        print("Invalid payment.")
        return

    confirm = input(
        "Confirm booking? (y/n): "
    ).lower()

    if confirm != "y":
        print("Booking cancelled.")
        return

    bid = booking_id()

    while find_booking(bid):
        bid = booking_id()

    booking = {
        "id": bid,
        "name": name,
        "phone": phone,
        "email": email,
        "movie_id": movie["id"],
        "movie": movie["name"],
        "show": show,
        "seats": seats,
        "amount": round(total, 2),
        "payment": payment,
        "status": "Confirmed",
        "date": str(datetime.datetime.now())
    }

    bookings.append(booking)

    print()
    line()
    print("              BOOKING SUCCESSFUL")
    line()

    print("Booking ID:", bid)
    print("Movie:", movie["name"])
    print("Seats:", ", ".join(seats))
    print("Amount: ₹", round(total, 2))

    pause()


# ----------------------- SEARCH -----------------------------

def find_booking(bid):

    for booking in bookings:
        if booking["id"].upper() == bid.upper():
            return booking

    return None


def search_booking():

    line()
    print("                 SEARCH BOOKING")
    line()

    bid = input("Enter Booking ID: ")

    booking = find_booking(bid)

    if booking:
        show_booking(booking)

    else:
        print("Booking not found.")

    pause()


def show_booking(booking):

    line()

    print("Booking ID :", booking["id"])
    print("Customer   :", booking["name"])
    print("Phone      :", booking["phone"])
    print("Movie      :", booking["movie"])
    print("Show       :", booking["show"])
    print("Seats      :", ", ".join(booking["seats"]))
    print("Amount     : ₹", booking["amount"])
    print("Payment    :", booking["payment"])
    print("Status     :", booking["status"])
    print("Date       :", booking["date"])

    line()


# ----------------------- CANCEL -----------------------------

def cancel_booking():

    line()
    print("                 CANCEL BOOKING")
    line()

    bid = input("Enter Booking ID: ")

    booking = find_booking(bid)

    if booking is None:
        print("Booking not found.")
        pause()
        return

    show_booking(booking)

    if booking["status"] == "Cancelled":
        print("Already cancelled.")
        pause()
        return

    choice = input(
        "Cancel this booking? (y/n): "
    ).lower()

    if choice == "y":
        booking["status"] = "Cancelled"
        print("Booking cancelled.")

    else:
        print("Cancellation stopped.")

    pause()


# ----------------------- HISTORY ----------------------------

def history():

    line()
    print("                BOOKING HISTORY")
    line()

    if not bookings:
        print("No bookings.")
        pause()
        return

    for booking in bookings:

        print(
            booking["id"],
            "|",
            booking["name"],
            "|",
            booking["movie"],
            "|",
            booking["status"],
            "| ₹",
            booking["amount"]
        )

    pause()


# ----------------------- MY BOOKINGS ------------------------

def my_bookings():

    phone = input(
        "Enter your phone number: "
    )

    found = False

    for booking in bookings:

        if booking["phone"] == phone:
            show_booking(booking)
            found = True

    if not found:
        print("No bookings found.")

    pause()


# ----------------------- SEARCH MOVIE -----------------------

def search_movie():

    keyword = input(
        "Enter movie name, language or genre: "
    ).lower()

    found = False

    for movie in movies:

        if (
            keyword in movie["name"].lower()
            or keyword in movie["language"].lower()
            or keyword in movie["genre"].lower()
        ):

            print(
                movie["id"],
                "-",
                movie["name"],
                "|",
                movie["language"],
                "|",
                movie["genre"]
            )

            found = True

    if not found:
        print("No movie found.")

    pause()


# ----------------------- ADMIN ------------------------------

def admin_login():

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":

        print("Login successful.")

        admin_menu()

    else:
        print("Wrong username/password.")

        pause()


def add_movie():

    line()
    print("                 ADD MOVIE")
    line()

    name = input("Movie name: ")
    language = input("Language: ")
    genre = input("Genre: ")

    while True:

        try:
            price = int(
                input("Ticket price: ")
            )

            if price > 0:
                break

        except ValueError:
            pass

        print("Enter valid price.")

    new_id = max(
        movie["id"]
        for movie in movies
    ) + 1

    movies.append({
        "id": new_id,
        "name": name,
        "language": language,
        "genre": genre,
        "price": price
    })

    shows[new_id] = [
        "10:00 AM",
        "2:00 PM",
        "6:00 PM",
        "9:00 PM"
    ]

    print("Movie added successfully.")

    pause()


def all_bookings():

    if not bookings:
        print("No bookings.")

    else:

        for booking in bookings:
            show_booking(booking)

    pause()


def revenue():

    total = 0

    for booking in bookings:

        if booking["status"] == "Confirmed":
            total += booking["amount"]

    line()
    print("Total Revenue: ₹", round(total, 2))
    line()

    pause()


def admin_menu():

    while True:

        line()
        print("                  ADMIN MENU")
        line()

        print("1. Add Movie")
        print("2. View Bookings")
        print("3. Revenue")
        print("4. Display Movies")
        print("5. Logout")

        choice = input(
            "Enter choice: "
        )

        if choice == "1":
            add_movie()

        elif choice == "2":
            all_bookings()

        elif choice == "3":
            revenue()

        elif choice == "4":
            display_movies()
            pause()

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")


# ----------------------- MAIN MENU --------------------------

def main():

    while True:

        print()
        line()
        print("       MOVIE TICKET BOOKING SYSTEM")
        line()

        print("1. Display Movies")
        print("2. Search Movie")
        print("3. Book Ticket")
        print("4. Search Booking")
        print("5. Cancel Booking")
        print("6. Booking History")
        print("7. My Bookings")
        print("8. Admin Login")
        print("9. Exit")

        line()

        choice = input(
            "Enter choice: "
        )

        if choice == "1":

            display_movies()
            pause()

        elif choice == "2":

            search_movie()

        elif choice == "3":

            book_ticket()

        elif choice == "4":

            search_booking()

        elif choice == "5":

            cancel_booking()

        elif choice == "6":

            history()

        elif choice == "7":

            my_bookings()

        elif choice == "8":

            admin_login()

        elif choice == "9":

            print()
            print("Thank you for using the system!")
            break

        else:

            print("Invalid choice.")


# ----------------------- START ------------------------------

if __name__ == "__main__":
    main()