class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()
        self.entry_hall(self)

    def _initialize_seats(self):
        for row in range(1, self._rows+1):
            self._seats[row] = [0] * self._cols

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [[0]*self._cols for _ in range(self._rows)]

    def book_seats(self, show_id, seat_list):
        if show_id not in self._seats:
            raise ValueError("Invalid show ID.")
        for row, col in seat_list:
            if not (1 <= row <= self._rows) or not (1 <= col <= self._cols):
                raise ValueError("Invalid seat.")
            if self._seats[show_id][row-1][col-1]:
                raise ValueError(
                    "Seat is already booked. Please try another seats")
            self._seats[show_id][row-1][col-1] = 1

    def view_show_list(self):
        for movie in self._show_list:
            print(movie)

    def view_available_seats(self, show_id):
        if show_id not in self._seats:
            raise ValueError("Invalid show ID.")
        for row in self._seats[show_id]:
            print(row)


hall = Hall(7, 7, 1)
hall.entry_show(111, "Apocalypto", "7.00 PM")
hall.entry_show(112, "X-man", "9.00 PM")
hall.entry_show(113, "Kiki's Delivery Service", "11.00 PM")

while True:
    print("1. View All Show")
    print("2. View Available Seats")
    print("3. Book a ticket")
    print("4. Exit")
    print("Enter Option: ")
    n = int(input())
    if n == 1:
        hall.view_show_list()
    elif n == 2:
        try:
            show_id = int(input("Enter show ID: "))
            hall.view_available_seats(show_id)
        except ValueError as err:
            print(f'Sorry: {err} Please Try again')
    elif n == 3:
        try:
            print("Enter Movie ID: ")
            id = int(input())
            print("Enter Seat Row: ")
            seat_row = int(input())
            print("Enter Seat Col: ")
            seat_col = int(input())
            hall.book_seats(id, [(seat_row, seat_col)])
            print(
                f'Successfully booked in {seat_row} No row and {seat_col} No column')
        except ValueError as err:
            print(f'Sorry: {err} Please try again')
    else:
        break
