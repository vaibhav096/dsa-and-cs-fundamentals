"""
================================================================================
                    REAL-WORLD OOP PROBLEMS - PYTHON IMPLEMENTATIONS
================================================================================
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from collections import defaultdict
import random
import string


# ==============================================================================
# 1. PARKING LOT SYSTEM
# ==============================================================================

class VehicleType(Enum):
    MOTORCYCLE = 1
    CAR = 2
    BUS = 3


class SpotSize(Enum):
    SMALL = 1      # Motorcycle
    MEDIUM = 2     # Car
    LARGE = 3      # Bus


class Vehicle(ABC):
    """Abstract base class for vehicles"""

    def __init__(self, license_plate: str):
        self.license_plate = license_plate
        self.vehicle_type: VehicleType = None

    @abstractmethod
    def get_required_spot_size(self) -> SpotSize:
        pass


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate)
        self.vehicle_type = VehicleType.MOTORCYCLE

    def get_required_spot_size(self) -> SpotSize:
        return SpotSize.SMALL


class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate)
        self.vehicle_type = VehicleType.CAR

    def get_required_spot_size(self) -> SpotSize:
        return SpotSize.MEDIUM


class Bus(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate)
        self.vehicle_type = VehicleType.BUS

    def get_required_spot_size(self) -> SpotSize:
        return SpotSize.LARGE


class ParkingSpot:
    """Individual parking spot"""

    def __init__(self, spot_id: str, size: SpotSize):
        self.spot_id = spot_id
        self.size = size
        self.vehicle: Optional[Vehicle] = None
        self.is_available = True

    def can_fit(self, vehicle: Vehicle) -> bool:
        """Check if vehicle can fit in this spot"""
        return (self.is_available and
                vehicle.get_required_spot_size().value <= self.size.value)

    def assign_vehicle(self, vehicle: Vehicle) -> bool:
        if self.can_fit(vehicle):
            self.vehicle = vehicle
            self.is_available = False
            return True
        return False

    def remove_vehicle(self) -> Optional[Vehicle]:
        vehicle = self.vehicle
        self.vehicle = None
        self.is_available = True
        return vehicle


class ParkingTicket:
    """Ticket issued when vehicle enters"""

    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = datetime.now()
        self.exit_time: Optional[datetime] = None
        self.amount_paid: float = 0

    def get_duration_hours(self) -> float:
        end_time = self.exit_time or datetime.now()
        duration = end_time - self.entry_time
        return duration.total_seconds() / 3600


class PricingStrategy(ABC):
    """Abstract pricing strategy"""

    @abstractmethod
    def calculate_fee(self, ticket: ParkingTicket) -> float:
        pass


class HourlyPricing(PricingStrategy):
    """Charge per hour based on vehicle type"""

    RATES = {
        VehicleType.MOTORCYCLE: 1.0,
        VehicleType.CAR: 2.0,
        VehicleType.BUS: 5.0
    }

    def calculate_fee(self, ticket: ParkingTicket) -> float:
        hours = max(1, int(ticket.get_duration_hours()) + 1)  # Minimum 1 hour
        rate = self.RATES.get(ticket.vehicle.vehicle_type, 2.0)
        return hours * rate


class ParkingFloor:
    """A floor in the parking lot"""

    def __init__(self, floor_number: int, spots: List[ParkingSpot]):
        self.floor_number = floor_number
        self.spots = spots

    def find_available_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        """Find first available spot for the vehicle"""
        for spot in self.spots:
            if spot.can_fit(vehicle):
                return spot
        return None

    def get_available_count(self) -> int:
        return sum(1 for spot in self.spots if spot.is_available)


class ParkingLot:
    """Main parking lot system"""

    def __init__(self, name: str):
        self.name = name
        self.floors: List[ParkingFloor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {}  # license_plate -> ticket
        self.pricing_strategy: PricingStrategy = HourlyPricing()

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingTicket]:
        """Park vehicle and return ticket"""
        if vehicle.license_plate in self.active_tickets:
            print(f"Vehicle {vehicle.license_plate} already parked!")
            return None

        # Find available spot
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.assign_vehicle(vehicle)
                ticket = ParkingTicket(vehicle, spot)
                self.active_tickets[vehicle.license_plate] = ticket
                print(f"Vehicle {vehicle.license_plate} parked at spot {spot.spot_id}")
                return ticket

        print(f"No available spot for {vehicle.license_plate}")
        return None

    def unpark_vehicle(self, license_plate: str) -> Optional[float]:
        """Remove vehicle and return fee"""
        if license_plate not in self.active_tickets:
            print(f"Vehicle {license_plate} not found!")
            return None

        ticket = self.active_tickets[license_plate]
        ticket.exit_time = datetime.now()
        fee = self.pricing_strategy.calculate_fee(ticket)

        ticket.spot.remove_vehicle()
        del self.active_tickets[license_plate]

        print(f"Vehicle {license_plate} unparked. Fee: ${fee:.2f}")
        return fee

    def get_total_available(self) -> int:
        return sum(floor.get_available_count() for floor in self.floors)


# Test Parking Lot
print("=" * 60)
print("PARKING LOT SYSTEM")
print("=" * 60)

# Create parking lot
lot = ParkingLot("City Center Parking")

# Create floors with spots
floor1_spots = [
    ParkingSpot("F1-S1", SpotSize.SMALL),
    ParkingSpot("F1-S2", SpotSize.SMALL),
    ParkingSpot("F1-M1", SpotSize.MEDIUM),
    ParkingSpot("F1-M2", SpotSize.MEDIUM),
    ParkingSpot("F1-L1", SpotSize.LARGE),
]
lot.add_floor(ParkingFloor(1, floor1_spots))

# Park vehicles
car1 = Car("ABC-123")
moto1 = Motorcycle("XYZ-789")
bus1 = Bus("BUS-001")

lot.park_vehicle(car1)
lot.park_vehicle(moto1)
lot.park_vehicle(bus1)

print(f"\nAvailable spots: {lot.get_total_available()}")

# Unpark
lot.unpark_vehicle("ABC-123")
print(f"Available spots after unpark: {lot.get_total_available()}")


# ==============================================================================
# 2. LIBRARY MANAGEMENT SYSTEM
# ==============================================================================

print("\n" + "=" * 60)
print("LIBRARY MANAGEMENT SYSTEM")
print("=" * 60)


class BookStatus(Enum):
    AVAILABLE = "available"
    BORROWED = "borrowed"
    RESERVED = "reserved"


class Book:
    """Book metadata"""

    def __init__(self, isbn: str, title: str, author: str, subject: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.subject = subject
        self.copies: List['BookItem'] = []

    def add_copy(self, copy: 'BookItem'):
        copy.book = self
        self.copies.append(copy)

    def get_available_copies(self) -> List['BookItem']:
        return [c for c in self.copies if c.status == BookStatus.AVAILABLE]


class BookItem:
    """Physical copy of a book"""

    def __init__(self, barcode: str):
        self.barcode = barcode
        self.book: Optional[Book] = None
        self.status = BookStatus.AVAILABLE
        self.rack_location: str = ""

    def checkout(self):
        self.status = BookStatus.BORROWED

    def checkin(self):
        self.status = BookStatus.AVAILABLE


class Member:
    """Library member"""
    MAX_BOOKS = 5
    LOAN_DAYS = 14

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books: List['Loan'] = []
        self.total_fine: float = 0

    def can_borrow(self) -> bool:
        active_loans = [l for l in self.borrowed_books if not l.is_returned]
        return len(active_loans) < self.MAX_BOOKS

    def get_active_loans(self) -> List['Loan']:
        return [l for l in self.borrowed_books if not l.is_returned]


class Loan:
    """Book borrowing record"""

    def __init__(self, book_item: BookItem, member: Member):
        self.loan_id = ''.join(random.choices(string.digits, k=6))
        self.book_item = book_item
        self.member = member
        self.issue_date = datetime.now()
        self.due_date = self.issue_date + timedelta(days=Member.LOAN_DAYS)
        self.return_date: Optional[datetime] = None
        self.fine: float = 0
        self.is_returned = False

    def calculate_fine(self) -> float:
        """$1 per day overdue"""
        if self.return_date and self.return_date > self.due_date:
            overdue_days = (self.return_date - self.due_date).days
            return overdue_days * 1.0
        return 0

    def return_book(self):
        self.return_date = datetime.now()
        self.fine = self.calculate_fine()
        self.is_returned = True
        self.book_item.checkin()


class Library:
    """Library system"""

    def __init__(self, name: str):
        self.name = name
        self.books: Dict[str, Book] = {}  # isbn -> Book
        self.members: Dict[str, Member] = {}  # member_id -> Member

    def add_book(self, book: Book):
        self.books[book.isbn] = book

    def register_member(self, member: Member):
        self.members[member.member_id] = member

    def search_by_title(self, title: str) -> List[Book]:
        return [b for b in self.books.values()
                if title.lower() in b.title.lower()]

    def search_by_author(self, author: str) -> List[Book]:
        return [b for b in self.books.values()
                if author.lower() in b.author.lower()]

    def borrow_book(self, isbn: str, member_id: str) -> Optional[Loan]:
        if isbn not in self.books:
            print(f"Book {isbn} not found")
            return None

        if member_id not in self.members:
            print(f"Member {member_id} not found")
            return None

        member = self.members[member_id]
        book = self.books[isbn]

        if not member.can_borrow():
            print(f"{member.name} has reached borrowing limit")
            return None

        available = book.get_available_copies()
        if not available:
            print(f"No available copies of {book.title}")
            return None

        book_item = available[0]
        book_item.checkout()

        loan = Loan(book_item, member)
        member.borrowed_books.append(loan)

        print(f"{member.name} borrowed '{book.title}'")
        print(f"Due date: {loan.due_date.strftime('%Y-%m-%d')}")
        return loan

    def return_book(self, loan: Loan) -> float:
        loan.return_book()
        fine = loan.fine
        loan.member.total_fine += fine

        print(f"'{loan.book_item.book.title}' returned by {loan.member.name}")
        if fine > 0:
            print(f"Fine: ${fine:.2f}")
        return fine


# Test Library System
library = Library("City Library")

# Add books
book1 = Book("978-0-13-468599-1", "Clean Code", "Robert C. Martin", "Programming")
book1.add_copy(BookItem("CC-001"))
book1.add_copy(BookItem("CC-002"))

book2 = Book("978-0-201-63361-0", "Design Patterns", "Gang of Four", "Programming")
book2.add_copy(BookItem("DP-001"))

library.add_book(book1)
library.add_book(book2)

# Register members
member1 = Member("M001", "Alice")
member2 = Member("M002", "Bob")
library.register_member(member1)
library.register_member(member2)

# Borrow and return
loan1 = library.borrow_book("978-0-13-468599-1", "M001")
loan2 = library.borrow_book("978-0-201-63361-0", "M001")

print(f"\n{member1.name}'s active loans: {len(member1.get_active_loans())}")

# Return book
if loan1:
    library.return_book(loan1)


# ==============================================================================
# 3. ELEVATOR SYSTEM
# ==============================================================================

print("\n" + "=" * 60)
print("ELEVATOR SYSTEM")
print("=" * 60)


class ElevatorState(Enum):
    IDLE = "idle"
    MOVING_UP = "moving_up"
    MOVING_DOWN = "moving_down"


class Direction(Enum):
    UP = 1
    DOWN = -1
    NONE = 0


class Request:
    """Floor request"""

    def __init__(self, floor: int, direction: Direction = Direction.NONE):
        self.floor = floor
        self.direction = direction
        self.timestamp = datetime.now()


class Elevator:
    """Individual elevator"""

    def __init__(self, elevator_id: int, min_floor: int = 0, max_floor: int = 10):
        self.elevator_id = elevator_id
        self.current_floor = 0
        self.state = ElevatorState.IDLE
        self.direction = Direction.NONE
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.requests: set = set()  # Set of floor numbers

    def add_request(self, floor: int):
        """Add floor to request list"""
        if self.min_floor <= floor <= self.max_floor:
            self.requests.add(floor)
            self._update_direction()

    def _update_direction(self):
        """Update direction based on requests"""
        if not self.requests:
            self.direction = Direction.NONE
            self.state = ElevatorState.IDLE
            return

        if self.direction == Direction.NONE:
            # Pick direction based on first request
            next_floor = min(self.requests, key=lambda x: abs(x - self.current_floor))
            if next_floor > self.current_floor:
                self.direction = Direction.UP
                self.state = ElevatorState.MOVING_UP
            elif next_floor < self.current_floor:
                self.direction = Direction.DOWN
                self.state = ElevatorState.MOVING_DOWN

    def move(self):
        """Move one floor in current direction"""
        if self.state == ElevatorState.IDLE:
            return

        # Move one floor
        if self.direction == Direction.UP:
            self.current_floor += 1
        elif self.direction == Direction.DOWN:
            self.current_floor -= 1

        print(f"Elevator {self.elevator_id} at floor {self.current_floor}")

        # Check if we should stop
        if self.current_floor in self.requests:
            self.requests.remove(self.current_floor)
            print(f"  -> Doors opening at floor {self.current_floor}")

        # Check if we need to change direction
        if self.direction == Direction.UP:
            above = [f for f in self.requests if f > self.current_floor]
            if not above:
                below = [f for f in self.requests if f < self.current_floor]
                if below:
                    self.direction = Direction.DOWN
                    self.state = ElevatorState.MOVING_DOWN
                else:
                    self.direction = Direction.NONE
                    self.state = ElevatorState.IDLE

        elif self.direction == Direction.DOWN:
            below = [f for f in self.requests if f < self.current_floor]
            if not below:
                above = [f for f in self.requests if f > self.current_floor]
                if above:
                    self.direction = Direction.UP
                    self.state = ElevatorState.MOVING_UP
                else:
                    self.direction = Direction.NONE
                    self.state = ElevatorState.IDLE

    def process_all_requests(self):
        """Process all requests until done"""
        while self.requests:
            self.move()


class ElevatorSystem:
    """Manages multiple elevators"""

    def __init__(self, num_elevators: int, num_floors: int):
        self.elevators = [
            Elevator(i, 0, num_floors) for i in range(num_elevators)
        ]
        self.num_floors = num_floors

    def request_elevator(self, floor: int, direction: Direction = Direction.NONE) -> Elevator:
        """Find best elevator for request"""
        best_elevator = None
        min_distance = float('inf')

        for elevator in self.elevators:
            # Prefer idle elevators or those moving towards this floor
            if elevator.state == ElevatorState.IDLE:
                distance = abs(elevator.current_floor - floor)
            elif (elevator.direction == Direction.UP and floor >= elevator.current_floor) or \
                 (elevator.direction == Direction.DOWN and floor <= elevator.current_floor):
                distance = abs(elevator.current_floor - floor)
            else:
                distance = float('inf')  # Moving away

            if distance < min_distance:
                min_distance = distance
                best_elevator = elevator

        if best_elevator:
            best_elevator.add_request(floor)
            print(f"Elevator {best_elevator.elevator_id} assigned to floor {floor}")

        return best_elevator


# Test Elevator System
system = ElevatorSystem(num_elevators=2, num_floors=10)

# Requests from different floors
system.request_elevator(5, Direction.UP)
system.request_elevator(3, Direction.DOWN)
system.request_elevator(7, Direction.UP)

# Process requests for first elevator
print("\nProcessing elevator 0:")
system.elevators[0].process_all_requests()


# ==============================================================================
# 4. SHOPPING CART SYSTEM
# ==============================================================================

print("\n" + "=" * 60)
print("SHOPPING CART SYSTEM")
print("=" * 60)


class Product:
    """Product in the store"""

    def __init__(self, product_id: str, name: str, price: float, category: str):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.inventory = 100  # Default inventory


class CartItem:
    """Item in shopping cart"""

    def __init__(self, product: Product, quantity: int = 1):
        self.product = product
        self.quantity = quantity

    def get_subtotal(self) -> float:
        return self.product.price * self.quantity

    def update_quantity(self, quantity: int):
        self.quantity = quantity


class DiscountStrategy(ABC):
    """Abstract discount strategy"""

    @abstractmethod
    def apply_discount(self, subtotal: float) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, subtotal: float) -> float:
        return subtotal

    def get_description(self) -> str:
        return "No discount"


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, subtotal: float) -> float:
        return subtotal * (1 - self.percentage / 100)

    def get_description(self) -> str:
        return f"{self.percentage}% off"


class FlatDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, subtotal: float) -> float:
        return max(0, subtotal - self.amount)

    def get_description(self) -> str:
        return f"${self.amount} off"


class ThresholdDiscount(DiscountStrategy):
    """Discount if subtotal exceeds threshold"""

    def __init__(self, threshold: float, percentage: float):
        self.threshold = threshold
        self.percentage = percentage

    def apply_discount(self, subtotal: float) -> float:
        if subtotal >= self.threshold:
            return subtotal * (1 - self.percentage / 100)
        return subtotal

    def get_description(self) -> str:
        return f"{self.percentage}% off on orders over ${self.threshold}"


class ShoppingCart:
    """Shopping cart"""

    TAX_RATE = 0.08  # 8% tax

    def __init__(self):
        self.items: Dict[str, CartItem] = {}  # product_id -> CartItem
        self.discount_strategy: DiscountStrategy = NoDiscount()

    def add_item(self, product: Product, quantity: int = 1):
        if product.product_id in self.items:
            self.items[product.product_id].quantity += quantity
        else:
            self.items[product.product_id] = CartItem(product, quantity)
        print(f"Added {quantity}x {product.name} to cart")

    def remove_item(self, product_id: str):
        if product_id in self.items:
            item = self.items.pop(product_id)
            print(f"Removed {item.product.name} from cart")

    def update_quantity(self, product_id: str, quantity: int):
        if product_id in self.items:
            if quantity <= 0:
                self.remove_item(product_id)
            else:
                self.items[product_id].quantity = quantity

    def set_discount(self, strategy: DiscountStrategy):
        self.discount_strategy = strategy
        print(f"Discount applied: {strategy.get_description()}")

    def get_subtotal(self) -> float:
        return sum(item.get_subtotal() for item in self.items.values())

    def get_total(self) -> float:
        subtotal = self.get_subtotal()
        after_discount = self.discount_strategy.apply_discount(subtotal)
        tax = after_discount * self.TAX_RATE
        return after_discount + tax

    def display_cart(self):
        print("\n--- Shopping Cart ---")
        for item in self.items.values():
            print(f"  {item.product.name} x{item.quantity} @ ${item.product.price:.2f} = ${item.get_subtotal():.2f}")

        subtotal = self.get_subtotal()
        print(f"\nSubtotal: ${subtotal:.2f}")

        after_discount = self.discount_strategy.apply_discount(subtotal)
        if after_discount != subtotal:
            print(f"Discount ({self.discount_strategy.get_description()}): -${subtotal - after_discount:.2f}")
            print(f"After discount: ${after_discount:.2f}")

        tax = after_discount * self.TAX_RATE
        print(f"Tax (8%): ${tax:.2f}")
        print(f"Total: ${self.get_total():.2f}")


# Test Shopping Cart
cart = ShoppingCart()

# Add products
laptop = Product("P001", "Laptop", 999.99, "Electronics")
mouse = Product("P002", "Wireless Mouse", 29.99, "Electronics")
book = Product("P003", "Python Book", 49.99, "Books")

cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(book, 1)

cart.display_cart()

# Apply discount
cart.set_discount(ThresholdDiscount(100, 10))  # 10% off on orders > $100
cart.display_cart()


# ==============================================================================
# 5. RESTAURANT ORDER SYSTEM
# ==============================================================================

print("\n" + "=" * 60)
print("RESTAURANT ORDER SYSTEM")
print("=" * 60)


class TableStatus(Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    RESERVED = "reserved"


class OrderStatus(Enum):
    PLACED = "placed"
    PREPARING = "preparing"
    READY = "ready"
    SERVED = "served"
    PAID = "paid"


class MenuItem:
    """Item on the menu"""

    def __init__(self, item_id: str, name: str, price: float,
                 category: str, prep_time: int = 10):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category  # Appetizer, Main, Dessert, Drink
        self.prep_time = prep_time  # minutes
        self.is_available = True


class OrderItem:
    """Item in an order"""

    def __init__(self, menu_item: MenuItem, quantity: int = 1,
                 special_instructions: str = ""):
        self.menu_item = menu_item
        self.quantity = quantity
        self.special_instructions = special_instructions

    def get_subtotal(self) -> float:
        return self.menu_item.price * self.quantity


class Table:
    """Restaurant table"""

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.status = TableStatus.AVAILABLE
        self.current_order: Optional['Order'] = None

    def occupy(self):
        self.status = TableStatus.OCCUPIED

    def vacate(self):
        self.status = TableStatus.AVAILABLE
        self.current_order = None


class Order:
    """Customer order"""

    def __init__(self, table: Optional[Table] = None, is_takeaway: bool = False):
        self.order_id = ''.join(random.choices(string.digits, k=6))
        self.table = table
        self.is_takeaway = is_takeaway
        self.items: List[OrderItem] = []
        self.status = OrderStatus.PLACED
        self.created_at = datetime.now()

        if table:
            table.current_order = self
            table.occupy()

    def add_item(self, menu_item: MenuItem, quantity: int = 1,
                 instructions: str = ""):
        item = OrderItem(menu_item, quantity, instructions)
        self.items.append(item)
        print(f"Added {quantity}x {menu_item.name} to order {self.order_id}")

    def get_subtotal(self) -> float:
        return sum(item.get_subtotal() for item in self.items)

    def update_status(self, status: OrderStatus):
        self.status = status
        print(f"Order {self.order_id} status: {status.value}")


class Bill:
    """Restaurant bill"""

    TAX_RATE = 0.10  # 10% tax

    def __init__(self, order: Order):
        self.order = order
        self.subtotal = order.get_subtotal()
        self.tax = self.subtotal * self.TAX_RATE
        self.tip: float = 0
        self.discount: float = 0
        self.total = self.subtotal + self.tax

    def add_tip(self, tip: float):
        self.tip = tip
        self.total = self.subtotal + self.tax + self.tip - self.discount

    def apply_discount(self, discount: float):
        self.discount = discount
        self.total = self.subtotal + self.tax + self.tip - self.discount

    def display(self):
        print(f"\n{'='*30}")
        print("         BILL")
        print(f"{'='*30}")
        print(f"Order: {self.order.order_id}")
        if self.order.table:
            print(f"Table: {self.order.table.table_number}")
        print("-" * 30)

        for item in self.order.items:
            print(f"{item.menu_item.name} x{item.quantity}")
            print(f"  ${item.get_subtotal():.2f}")

        print("-" * 30)
        print(f"Subtotal:  ${self.subtotal:.2f}")
        print(f"Tax (10%): ${self.tax:.2f}")
        if self.tip > 0:
            print(f"Tip:       ${self.tip:.2f}")
        if self.discount > 0:
            print(f"Discount:  -${self.discount:.2f}")
        print(f"{'='*30}")
        print(f"TOTAL:     ${self.total:.2f}")


class Restaurant:
    """Restaurant system"""

    def __init__(self, name: str):
        self.name = name
        self.menu: Dict[str, MenuItem] = {}
        self.tables: Dict[int, Table] = {}
        self.orders: List[Order] = []

    def add_menu_item(self, item: MenuItem):
        self.menu[item.item_id] = item

    def add_table(self, table: Table):
        self.tables[table.table_number] = table

    def get_available_tables(self) -> List[Table]:
        return [t for t in self.tables.values() if t.status == TableStatus.AVAILABLE]

    def create_order(self, table_number: Optional[int] = None) -> Order:
        table = self.tables.get(table_number) if table_number else None
        is_takeaway = table is None
        order = Order(table, is_takeaway)
        self.orders.append(order)
        print(f"Order {order.order_id} created" +
              (f" for table {table_number}" if table_number else " (Takeaway)"))
        return order

    def generate_bill(self, order: Order) -> Bill:
        return Bill(order)


# Test Restaurant System
restaurant = Restaurant("The Python Cafe")

# Add menu items
restaurant.add_menu_item(MenuItem("M001", "Burger", 12.99, "Main", 15))
restaurant.add_menu_item(MenuItem("M002", "Pizza", 14.99, "Main", 20))
restaurant.add_menu_item(MenuItem("D001", "Coke", 2.99, "Drink", 1))
restaurant.add_menu_item(MenuItem("D002", "Coffee", 3.99, "Drink", 5))
restaurant.add_menu_item(MenuItem("A001", "Fries", 4.99, "Appetizer", 8))

# Add tables
restaurant.add_table(Table(1, 2))
restaurant.add_table(Table(2, 4))
restaurant.add_table(Table(3, 6))

# Create order
order = restaurant.create_order(table_number=2)
order.add_item(restaurant.menu["M001"], 2)
order.add_item(restaurant.menu["M002"], 1)
order.add_item(restaurant.menu["D001"], 3)
order.add_item(restaurant.menu["A001"], 1)

# Update status
order.update_status(OrderStatus.PREPARING)
order.update_status(OrderStatus.READY)
order.update_status(OrderStatus.SERVED)

# Generate bill
bill = restaurant.generate_bill(order)
bill.add_tip(5.00)
bill.display()


print("\n" + "=" * 60)
print("ALL REAL-WORLD OOP EXAMPLES COMPLETED!")
print("=" * 60)
