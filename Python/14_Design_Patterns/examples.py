"""
================================================================================
                    DESIGN PATTERNS - PYTHON EXAMPLES
================================================================================
"""

from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

# ==============================================================================
# 1. SINGLETON PATTERN - Database Connection
# ==============================================================================

class DatabaseConnection:
    """Singleton database connection"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.connection_string = "mongodb://localhost:27017"
        self.connected = False
        print("Database instance created")

    def connect(self):
        if not self.connected:
            print(f"Connecting to {self.connection_string}")
            self.connected = True

    def disconnect(self):
        if self.connected:
            print("Disconnecting...")
            self.connected = False

# Test Singleton
print("=" * 50)
print("SINGLETON PATTERN TEST")
print("=" * 50)
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"Same instance? {db1 is db2}")  # True


# ==============================================================================
# 2. FACTORY PATTERN - Notification System
# ==============================================================================

class Notification(ABC):
    """Abstract notification"""
    @abstractmethod
    def send(self, message: str) -> str:
        pass

class EmailNotification(Notification):
    def __init__(self, email: str):
        self.email = email

    def send(self, message: str) -> str:
        return f"Email sent to {self.email}: {message}"

class SMSNotification(Notification):
    def __init__(self, phone: str):
        self.phone = phone

    def send(self, message: str) -> str:
        return f"SMS sent to {self.phone}: {message}"

class PushNotification(Notification):
    def __init__(self, device_id: str):
        self.device_id = device_id

    def send(self, message: str) -> str:
        return f"Push sent to device {self.device_id}: {message}"

class NotificationFactory:
    """Factory for creating notifications"""

    @staticmethod
    def create(notification_type: str, recipient: str) -> Notification:
        if notification_type == "email":
            return EmailNotification(recipient)
        elif notification_type == "sms":
            return SMSNotification(recipient)
        elif notification_type == "push":
            return PushNotification(recipient)
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# Test Factory
print("\n" + "=" * 50)
print("FACTORY PATTERN TEST")
print("=" * 50)
email = NotificationFactory.create("email", "user@example.com")
sms = NotificationFactory.create("sms", "123-456-7890")
print(email.send("Hello!"))
print(sms.send("Hello!"))


# ==============================================================================
# 3. BUILDER PATTERN - Query Builder
# ==============================================================================

class SQLQuery:
    """SQL Query object"""
    def __init__(self):
        self.select_clause = "*"
        self.from_clause = ""
        self.where_clauses = []
        self.order_by_clause = ""
        self.limit_clause = ""

    def __str__(self):
        query = f"SELECT {self.select_clause} FROM {self.from_clause}"
        if self.where_clauses:
            query += " WHERE " + " AND ".join(self.where_clauses)
        if self.order_by_clause:
            query += f" ORDER BY {self.order_by_clause}"
        if self.limit_clause:
            query += f" LIMIT {self.limit_clause}"
        return query

class QueryBuilder:
    """Builder for SQL queries"""

    def __init__(self):
        self.query = SQLQuery()

    def select(self, columns: str):
        self.query.select_clause = columns
        return self

    def from_table(self, table: str):
        self.query.from_clause = table
        return self

    def where(self, condition: str):
        self.query.where_clauses.append(condition)
        return self

    def order_by(self, column: str, direction: str = "ASC"):
        self.query.order_by_clause = f"{column} {direction}"
        return self

    def limit(self, count: int):
        self.query.limit_clause = str(count)
        return self

    def build(self) -> SQLQuery:
        return self.query

# Test Builder
print("\n" + "=" * 50)
print("BUILDER PATTERN TEST")
print("=" * 50)
query = (QueryBuilder()
    .select("id, name, email")
    .from_table("users")
    .where("age > 18")
    .where("status = 'active'")
    .order_by("name", "ASC")
    .limit(10)
    .build())
print(query)


# ==============================================================================
# 4. STRATEGY PATTERN - Pricing Strategy
# ==============================================================================

class PricingStrategy(ABC):
    """Abstract pricing strategy"""
    @abstractmethod
    def calculate(self, base_price: float, quantity: int) -> float:
        pass

class RegularPricing(PricingStrategy):
    def calculate(self, base_price: float, quantity: int) -> float:
        return base_price * quantity

class BulkPricing(PricingStrategy):
    """10% discount for 10+ items"""
    def calculate(self, base_price: float, quantity: int) -> float:
        total = base_price * quantity
        if quantity >= 10:
            total *= 0.90  # 10% discount
        return total

class PremiumPricing(PricingStrategy):
    """20% discount always"""
    def calculate(self, base_price: float, quantity: int) -> float:
        return base_price * quantity * 0.80

class SeasonalPricing(PricingStrategy):
    """Seasonal discount based on month"""
    def __init__(self, discount_months: List[int], discount_percent: float):
        self.discount_months = discount_months
        self.discount_percent = discount_percent

    def calculate(self, base_price: float, quantity: int) -> float:
        total = base_price * quantity
        current_month = datetime.now().month
        if current_month in self.discount_months:
            total *= (1 - self.discount_percent / 100)
        return total

class PriceCalculator:
    """Context that uses pricing strategy"""

    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PricingStrategy):
        self.strategy = strategy

    def calculate_price(self, base_price: float, quantity: int) -> float:
        return self.strategy.calculate(base_price, quantity)

# Test Strategy
print("\n" + "=" * 50)
print("STRATEGY PATTERN TEST")
print("=" * 50)
calculator = PriceCalculator(RegularPricing())
print(f"Regular (5 items @ $10): ${calculator.calculate_price(10, 5)}")

calculator.set_strategy(BulkPricing())
print(f"Bulk (15 items @ $10): ${calculator.calculate_price(10, 15)}")

calculator.set_strategy(PremiumPricing())
print(f"Premium (5 items @ $10): ${calculator.calculate_price(10, 5)}")


# ==============================================================================
# 5. OBSERVER PATTERN - Stock Price Monitor
# ==============================================================================

class StockObserver(ABC):
    """Observer interface"""
    @abstractmethod
    def update(self, stock: str, price: float):
        pass

class StockMarket:
    """Subject - Stock market"""

    def __init__(self):
        self._observers: List[StockObserver] = []
        self._stocks: Dict[str, float] = {}

    def attach(self, observer: StockObserver):
        self._observers.append(observer)

    def detach(self, observer: StockObserver):
        self._observers.remove(observer)

    def notify(self, stock: str, price: float):
        for observer in self._observers:
            observer.update(stock, price)

    def set_price(self, stock: str, price: float):
        old_price = self._stocks.get(stock, 0)
        self._stocks[stock] = price
        if old_price != price:
            self.notify(stock, price)

class PriceAlert(StockObserver):
    """Alert when price crosses threshold"""

    def __init__(self, stock: str, threshold: float, alert_type: str = "above"):
        self.stock = stock
        self.threshold = threshold
        self.alert_type = alert_type

    def update(self, stock: str, price: float):
        if stock != self.stock:
            return
        if self.alert_type == "above" and price > self.threshold:
            print(f"ALERT: {stock} is above ${self.threshold}! Current: ${price}")
        elif self.alert_type == "below" and price < self.threshold:
            print(f"ALERT: {stock} is below ${self.threshold}! Current: ${price}")

class PriceLogger(StockObserver):
    """Log all price changes"""

    def update(self, stock: str, price: float):
        print(f"LOG: {stock} price changed to ${price}")

# Test Observer
print("\n" + "=" * 50)
print("OBSERVER PATTERN TEST")
print("=" * 50)
market = StockMarket()
market.attach(PriceLogger())
market.attach(PriceAlert("AAPL", 150, "above"))
market.attach(PriceAlert("GOOGL", 100, "below"))

market.set_price("AAPL", 145)
market.set_price("AAPL", 155)  # Triggers alert
market.set_price("GOOGL", 95)  # Triggers alert


# ==============================================================================
# 6. DECORATOR PATTERN - Text Formatting
# ==============================================================================

class TextComponent(ABC):
    """Abstract text component"""
    @abstractmethod
    def render(self) -> str:
        pass

class PlainText(TextComponent):
    """Concrete component"""
    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text

class TextDecorator(TextComponent):
    """Base decorator"""
    def __init__(self, component: TextComponent):
        self._component = component

    def render(self) -> str:
        return self._component.render()

class BoldDecorator(TextDecorator):
    def render(self) -> str:
        return f"<b>{self._component.render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self) -> str:
        return f"<i>{self._component.render()}</i>"

class UnderlineDecorator(TextDecorator):
    def render(self) -> str:
        return f"<u>{self._component.render()}</u>"

class ColorDecorator(TextDecorator):
    def __init__(self, component: TextComponent, color: str):
        super().__init__(component)
        self.color = color

    def render(self) -> str:
        return f'<span style="color:{self.color}">{self._component.render()}</span>'

# Test Decorator
print("\n" + "=" * 50)
print("DECORATOR PATTERN TEST")
print("=" * 50)
text = PlainText("Hello World")
print(f"Plain: {text.render()}")

bold_text = BoldDecorator(text)
print(f"Bold: {bold_text.render()}")

styled_text = ColorDecorator(
    UnderlineDecorator(
        ItalicDecorator(
            BoldDecorator(text)
        )
    ),
    "red"
)
print(f"Fully styled: {styled_text.render()}")


# ==============================================================================
# 7. STATE PATTERN - Vending Machine
# ==============================================================================

class VendingState(ABC):
    """State interface"""
    @abstractmethod
    def insert_coin(self, machine):
        pass

    @abstractmethod
    def select_product(self, machine, product: str):
        pass

    @abstractmethod
    def dispense(self, machine):
        pass

class NoCoinState(VendingState):
    def insert_coin(self, machine):
        print("Coin inserted")
        machine.state = HasCoinState()

    def select_product(self, machine, product: str):
        print("Please insert coin first")

    def dispense(self, machine):
        print("Please insert coin first")

class HasCoinState(VendingState):
    def insert_coin(self, machine):
        print("Coin already inserted")

    def select_product(self, machine, product: str):
        print(f"Product {product} selected")
        machine.selected_product = product
        machine.state = DispensingState()

    def dispense(self, machine):
        print("Please select a product first")

class DispensingState(VendingState):
    def insert_coin(self, machine):
        print("Please wait, dispensing product")

    def select_product(self, machine, product: str):
        print("Please wait, dispensing product")

    def dispense(self, machine):
        print(f"Dispensing {machine.selected_product}")
        machine.selected_product = None
        machine.state = NoCoinState()

class VendingMachine:
    """Context - Vending Machine"""

    def __init__(self):
        self.state: VendingState = NoCoinState()
        self.selected_product: str = None

    def insert_coin(self):
        self.state.insert_coin(self)

    def select_product(self, product: str):
        self.state.select_product(self, product)

    def dispense(self):
        self.state.dispense(self)

# Test State
print("\n" + "=" * 50)
print("STATE PATTERN TEST")
print("=" * 50)
vm = VendingMachine()
vm.select_product("Cola")  # Should fail - no coin
vm.insert_coin()
vm.select_product("Cola")
vm.dispense()
vm.dispense()  # Should fail - back to no coin state


# ==============================================================================
# 8. COMMAND PATTERN - Smart Home
# ==============================================================================

class Command(ABC):
    """Command interface"""
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    """Receiver"""
    def __init__(self, location: str):
        self.location = location
        self.is_on = False

    def on(self):
        self.is_on = True
        print(f"{self.location} light is ON")

    def off(self):
        self.is_on = False
        print(f"{self.location} light is OFF")

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class RemoteControl:
    """Invoker with undo functionality"""

    def __init__(self):
        self.history: List[Command] = []

    def execute(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("Nothing to undo")

# Test Command
print("\n" + "=" * 50)
print("COMMAND PATTERN TEST")
print("=" * 50)
living_room = Light("Living Room")
bedroom = Light("Bedroom")

remote = RemoteControl()
remote.execute(LightOnCommand(living_room))
remote.execute(LightOnCommand(bedroom))
remote.undo()  # Turns bedroom off
remote.undo()  # Turns living room off


print("\n" + "=" * 50)
print("ALL TESTS COMPLETED!")
print("=" * 50)
