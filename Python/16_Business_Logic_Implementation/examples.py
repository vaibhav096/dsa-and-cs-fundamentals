"""
================================================================================
                    COMPLEX BUSINESS LOGIC IMPLEMENTATIONS
================================================================================
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta, date
from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass
import random
import string


# ==============================================================================
# 1. SLAB-BASED PRICING - INCOME TAX CALCULATOR
# ==============================================================================

print("=" * 60)
print("1. SLAB-BASED PRICING - INCOME TAX")
print("=" * 60)


@dataclass
class TaxSlab:
    """Represents a tax slab"""
    lower_limit: Decimal
    upper_limit: Optional[Decimal]  # None for last slab (unlimited)
    rate: Decimal  # As percentage (e.g., 10 for 10%)


class IncomeTaxCalculator:
    """Calculate income tax using slab-based rates"""

    def __init__(self, slabs: List[TaxSlab]):
        self.slabs = sorted(slabs, key=lambda x: x.lower_limit)

    def calculate_tax(self, income: Decimal) -> Dict:
        """Calculate tax with breakdown"""
        if income <= 0:
            return {"total_tax": Decimal("0"), "breakdown": [], "effective_rate": Decimal("0")}

        breakdown = []
        total_tax = Decimal("0")
        remaining_income = income

        for slab in self.slabs:
            if remaining_income <= 0:
                break

            # Calculate taxable amount in this slab
            slab_width = (slab.upper_limit - slab.lower_limit
                         if slab.upper_limit else remaining_income)

            taxable_in_slab = min(remaining_income, slab_width)
            tax_in_slab = (taxable_in_slab * slab.rate / 100).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )

            if taxable_in_slab > 0:
                breakdown.append({
                    "slab": f"${slab.lower_limit:,} - ${slab.upper_limit:,}" if slab.upper_limit else f"${slab.lower_limit:,}+",
                    "rate": f"{slab.rate}%",
                    "taxable_amount": taxable_in_slab,
                    "tax": tax_in_slab
                })

            total_tax += tax_in_slab
            remaining_income -= taxable_in_slab

        effective_rate = (total_tax / income * 100).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

        return {
            "income": income,
            "total_tax": total_tax,
            "breakdown": breakdown,
            "effective_rate": effective_rate
        }

    def display_calculation(self, income: Decimal):
        result = self.calculate_tax(income)

        print(f"\nIncome: ${result['income']:,}")
        print("-" * 40)

        for item in result['breakdown']:
            print(f"  {item['slab']}: ${item['taxable_amount']:,} @ {item['rate']} = ${item['tax']:,}")

        print("-" * 40)
        print(f"  Total Tax: ${result['total_tax']:,}")
        print(f"  Effective Tax Rate: {result['effective_rate']}%")


# Define tax slabs
tax_slabs = [
    TaxSlab(Decimal("0"), Decimal("10000"), Decimal("0")),
    TaxSlab(Decimal("10000"), Decimal("40000"), Decimal("10")),
    TaxSlab(Decimal("40000"), Decimal("100000"), Decimal("20")),
    TaxSlab(Decimal("100000"), None, Decimal("30")),  # No upper limit
]

calculator = IncomeTaxCalculator(tax_slabs)

# Test with different incomes
calculator.display_calculation(Decimal("25000"))
calculator.display_calculation(Decimal("75000"))
calculator.display_calculation(Decimal("150000"))


# ==============================================================================
# 2. ELECTRICITY BILLING WITH SLABS
# ==============================================================================

print("\n" + "=" * 60)
print("2. ELECTRICITY BILLING")
print("=" * 60)


@dataclass
class ConsumptionSlab:
    units_from: int
    units_to: Optional[int]
    rate_per_unit: Decimal


class ElectricityBillCalculator:
    """Calculate electricity bill with slab rates and fixed charges"""

    def __init__(self, slabs: List[ConsumptionSlab],
                 fixed_charge: Decimal = Decimal("50"),
                 tax_rate: Decimal = Decimal("5")):
        self.slabs = sorted(slabs, key=lambda x: x.units_from)
        self.fixed_charge = fixed_charge
        self.tax_rate = tax_rate

    def calculate_bill(self, units_consumed: int) -> Dict:
        if units_consumed < 0:
            raise ValueError("Units cannot be negative")

        breakdown = []
        energy_charge = Decimal("0")
        remaining_units = units_consumed

        for slab in self.slabs:
            if remaining_units <= 0:
                break

            slab_size = ((slab.units_to - slab.units_from)
                        if slab.units_to else remaining_units)

            units_in_slab = min(remaining_units, slab_size)
            charge = units_in_slab * slab.rate_per_unit

            if units_in_slab > 0:
                breakdown.append({
                    "range": f"{slab.units_from}-{slab.units_to or '∞'} units",
                    "units": units_in_slab,
                    "rate": slab.rate_per_unit,
                    "charge": charge
                })

            energy_charge += charge
            remaining_units -= units_in_slab

        subtotal = energy_charge + self.fixed_charge
        tax = (subtotal * self.tax_rate / 100).quantize(Decimal("0.01"))
        total = subtotal + tax

        return {
            "units_consumed": units_consumed,
            "energy_charge": energy_charge,
            "fixed_charge": self.fixed_charge,
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
            "breakdown": breakdown
        }

    def display_bill(self, units: int):
        bill = self.calculate_bill(units)

        print(f"\n{'='*40}")
        print("       ELECTRICITY BILL")
        print(f"{'='*40}")
        print(f"Units Consumed: {bill['units_consumed']}")
        print("-" * 40)

        for item in bill['breakdown']:
            print(f"  {item['range']}: {item['units']} × ${item['rate']} = ${item['charge']:.2f}")

        print("-" * 40)
        print(f"  Energy Charge: ${bill['energy_charge']:.2f}")
        print(f"  Fixed Charge:  ${bill['fixed_charge']:.2f}")
        print(f"  Subtotal:      ${bill['subtotal']:.2f}")
        print(f"  Tax ({self.tax_rate}%):     ${bill['tax']:.2f}")
        print(f"{'='*40}")
        print(f"  TOTAL:         ${bill['total']:.2f}")


# Define consumption slabs
electricity_slabs = [
    ConsumptionSlab(0, 100, Decimal("3.50")),      # First 100 units
    ConsumptionSlab(100, 300, Decimal("4.50")),    # 101-300 units
    ConsumptionSlab(300, 500, Decimal("6.00")),    # 301-500 units
    ConsumptionSlab(500, None, Decimal("7.50")),   # Above 500 units
]

electricity_calc = ElectricityBillCalculator(electricity_slabs)

electricity_calc.display_bill(150)
electricity_calc.display_bill(450)


# ==============================================================================
# 3. MULTI-TIER DISCOUNT SYSTEM
# ==============================================================================

print("\n" + "=" * 60)
print("3. MULTI-TIER DISCOUNT SYSTEM")
print("=" * 60)


class DiscountType(Enum):
    PERCENTAGE = "percentage"
    FLAT = "flat"


@dataclass
class Discount:
    name: str
    discount_type: DiscountType
    value: Decimal
    min_order_amount: Decimal = Decimal("0")
    max_discount: Optional[Decimal] = None
    is_stackable: bool = False
    priority: int = 0  # Lower = applied first


class DiscountEngine:
    """Engine for calculating and applying multiple discounts"""

    def __init__(self, max_total_discount_percent: Decimal = Decimal("50")):
        self.max_total_discount_percent = max_total_discount_percent

    def calculate_discount(self, discount: Discount, amount: Decimal) -> Decimal:
        """Calculate single discount amount"""
        if amount < discount.min_order_amount:
            return Decimal("0")

        if discount.discount_type == DiscountType.PERCENTAGE:
            disc = (amount * discount.value / 100)
        else:  # FLAT
            disc = discount.value

        # Apply max discount cap if exists
        if discount.max_discount:
            disc = min(disc, discount.max_discount)

        return disc.quantize(Decimal("0.01"))

    def apply_discounts(self, amount: Decimal,
                        discounts: List[Discount],
                        mode: str = "best") -> Dict:
        """
        Apply discounts to amount
        mode: 'best' (single best), 'stack' (all stackable), 'all' (all applicable)
        """
        applicable = [d for d in discounts if amount >= d.min_order_amount]
        applicable.sort(key=lambda x: x.priority)

        if mode == "best":
            # Find single best discount
            best_discount = None
            best_amount = Decimal("0")

            for d in applicable:
                disc_amount = self.calculate_discount(d, amount)
                if disc_amount > best_amount:
                    best_amount = disc_amount
                    best_discount = d

            applied = [{"name": best_discount.name, "amount": best_amount}] if best_discount else []
            total_discount = best_amount

        elif mode == "stack":
            # Apply all stackable discounts
            applied = []
            current_amount = amount
            total_discount = Decimal("0")

            for d in applicable:
                if d.is_stackable or len(applied) == 0:
                    disc_amount = self.calculate_discount(d, current_amount)
                    if disc_amount > 0:
                        applied.append({"name": d.name, "amount": disc_amount})
                        total_discount += disc_amount
                        current_amount -= disc_amount

        else:  # all
            applied = []
            total_discount = Decimal("0")
            for d in applicable:
                disc_amount = self.calculate_discount(d, amount)
                applied.append({"name": d.name, "amount": disc_amount})
                total_discount += disc_amount

        # Apply max discount cap
        max_allowed = amount * self.max_total_discount_percent / 100
        if total_discount > max_allowed:
            total_discount = max_allowed

        final_amount = amount - total_discount

        return {
            "original_amount": amount,
            "discounts_applied": applied,
            "total_discount": total_discount,
            "final_amount": final_amount
        }


# Test discount system
engine = DiscountEngine()

discounts = [
    Discount("New User 10%", DiscountType.PERCENTAGE, Decimal("10"),
             is_stackable=False, priority=1),
    Discount("$20 Off", DiscountType.FLAT, Decimal("20"),
             min_order_amount=Decimal("100"), is_stackable=True, priority=2),
    Discount("Bulk 15%", DiscountType.PERCENTAGE, Decimal("15"),
             min_order_amount=Decimal("200"), max_discount=Decimal("50"),
             is_stackable=True, priority=3),
]

amount = Decimal("250")

print(f"\nOrder Amount: ${amount}")
print("-" * 40)

# Best single discount
result = engine.apply_discounts(amount, discounts, mode="best")
print(f"\nBest Single Discount:")
for d in result["discounts_applied"]:
    print(f"  {d['name']}: -${d['amount']}")
print(f"  Final: ${result['final_amount']}")

# Stacked discounts
result = engine.apply_discounts(amount, discounts, mode="stack")
print(f"\nStacked Discounts:")
for d in result["discounts_applied"]:
    print(f"  {d['name']}: -${d['amount']}")
print(f"  Total Discount: ${result['total_discount']}")
print(f"  Final: ${result['final_amount']}")


# ==============================================================================
# 4. MOVIE TICKET BOOKING WITH DYNAMIC PRICING
# ==============================================================================

print("\n" + "=" * 60)
print("4. MOVIE TICKET BOOKING SYSTEM")
print("=" * 60)


class SeatType(Enum):
    REGULAR = "regular"
    PREMIUM = "premium"
    VIP = "vip"


class ShowTime(Enum):
    MORNING = "morning"      # Before 12 PM
    AFTERNOON = "afternoon"  # 12 PM - 5 PM
    EVENING = "evening"      # 5 PM - 9 PM
    NIGHT = "night"          # After 9 PM


@dataclass
class Seat:
    row: str
    number: int
    seat_type: SeatType
    is_booked: bool = False


class MovieShow:
    """A movie showing"""

    BASE_PRICES = {
        SeatType.REGULAR: Decimal("10"),
        SeatType.PREMIUM: Decimal("15"),
        SeatType.VIP: Decimal("25"),
    }

    TIME_MULTIPLIERS = {
        ShowTime.MORNING: Decimal("0.8"),    # 20% off
        ShowTime.AFTERNOON: Decimal("1.0"),
        ShowTime.EVENING: Decimal("1.2"),    # 20% extra
        ShowTime.NIGHT: Decimal("1.1"),      # 10% extra
    }

    def __init__(self, movie_name: str, show_time: ShowTime,
                 is_weekend: bool = False, is_3d: bool = False):
        self.movie_name = movie_name
        self.show_time = show_time
        self.is_weekend = is_weekend
        self.is_3d = is_3d
        self.seats: Dict[str, Seat] = {}
        self._initialize_seats()

    def _initialize_seats(self):
        # Create seats: A1-A10 (VIP), B1-B10 (Premium), C1-C10 to E1-E10 (Regular)
        for i in range(1, 11):
            self.seats[f"A{i}"] = Seat("A", i, SeatType.VIP)
        for i in range(1, 11):
            self.seats[f"B{i}"] = Seat("B", i, SeatType.PREMIUM)
        for row in ["C", "D", "E"]:
            for i in range(1, 11):
                self.seats[f"{row}{i}"] = Seat(row, i, SeatType.REGULAR)

    def get_seat_price(self, seat: Seat) -> Decimal:
        """Calculate price for a seat"""
        base = self.BASE_PRICES[seat.seat_type]

        # Apply time multiplier
        price = base * self.TIME_MULTIPLIERS[self.show_time]

        # Weekend surcharge
        if self.is_weekend:
            price *= Decimal("1.15")  # 15% extra

        # 3D surcharge
        if self.is_3d:
            price += Decimal("3")

        return price.quantize(Decimal("0.01"))

    def get_available_seats(self, seat_type: Optional[SeatType] = None) -> List[Seat]:
        seats = [s for s in self.seats.values() if not s.is_booked]
        if seat_type:
            seats = [s for s in seats if s.seat_type == seat_type]
        return seats


class TicketBooking:
    """Booking system"""

    CONVENIENCE_FEE = Decimal("1.50")
    TAX_RATE = Decimal("8")

    def __init__(self):
        self.bookings: Dict[str, Dict] = {}

    def book_tickets(self, show: MovieShow, seat_ids: List[str],
                     customer_id: str, is_first_booking: bool = False) -> Dict:
        """Book tickets and return booking details"""

        # Validate seats
        for seat_id in seat_ids:
            if seat_id not in show.seats:
                raise ValueError(f"Seat {seat_id} does not exist")
            if show.seats[seat_id].is_booked:
                raise ValueError(f"Seat {seat_id} is already booked")

        # Calculate prices
        ticket_details = []
        subtotal = Decimal("0")

        for seat_id in seat_ids:
            seat = show.seats[seat_id]
            price = show.get_seat_price(seat)
            ticket_details.append({
                "seat": seat_id,
                "type": seat.seat_type.value,
                "price": price
            })
            subtotal += price
            seat.is_booked = True

        # Convenience fee
        convenience_fee = self.CONVENIENCE_FEE * len(seat_ids)

        # First booking discount
        first_booking_discount = Decimal("0")
        if is_first_booking:
            first_booking_discount = (subtotal * Decimal("10") / 100).quantize(Decimal("0.01"))

        # Tax
        taxable = subtotal + convenience_fee - first_booking_discount
        tax = (taxable * self.TAX_RATE / 100).quantize(Decimal("0.01"))

        total = taxable + tax

        booking = {
            "booking_id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=8)),
            "movie": show.movie_name,
            "show_time": show.show_time.value,
            "tickets": ticket_details,
            "subtotal": subtotal,
            "convenience_fee": convenience_fee,
            "first_booking_discount": first_booking_discount,
            "tax": tax,
            "total": total,
            "customer_id": customer_id
        }

        self.bookings[booking["booking_id"]] = booking
        return booking

    def display_booking(self, booking: Dict):
        print(f"\n{'='*45}")
        print("        BOOKING CONFIRMATION")
        print(f"{'='*45}")
        print(f"Booking ID: {booking['booking_id']}")
        print(f"Movie: {booking['movie']}")
        print(f"Show: {booking['show_time'].title()}")
        print("-" * 45)
        print("Tickets:")
        for t in booking['tickets']:
            print(f"  Seat {t['seat']} ({t['type']}): ${t['price']}")
        print("-" * 45)
        print(f"  Subtotal:          ${booking['subtotal']:.2f}")
        print(f"  Convenience Fee:   ${booking['convenience_fee']:.2f}")
        if booking['first_booking_discount'] > 0:
            print(f"  First Booking:    -${booking['first_booking_discount']:.2f}")
        print(f"  Tax (8%):          ${booking['tax']:.2f}")
        print(f"{'='*45}")
        print(f"  TOTAL:             ${booking['total']:.2f}")


# Test movie booking
show = MovieShow("The Matrix 5", ShowTime.EVENING, is_weekend=True, is_3d=True)
booking_system = TicketBooking()

# Show available seats
available = show.get_available_seats(SeatType.VIP)
print(f"\nAvailable VIP seats: {[f'{s.row}{s.number}' for s in available[:5]]}...")

# Book tickets
booking = booking_system.book_tickets(
    show,
    ["A1", "A2", "B5"],
    customer_id="CUST001",
    is_first_booking=True
)
booking_system.display_booking(booking)


# ==============================================================================
# 5. SUBSCRIPTION BILLING WITH PRORATION
# ==============================================================================

print("\n" + "=" * 60)
print("5. SUBSCRIPTION BILLING")
print("=" * 60)


class SubscriptionPlan(Enum):
    BASIC = "basic"
    PRO = "pro"
    ENTERPRISE = "enterprise"


@dataclass
class Plan:
    name: SubscriptionPlan
    monthly_price: Decimal
    features: List[str]


class Subscription:
    """User subscription"""

    PLANS = {
        SubscriptionPlan.BASIC: Plan(
            SubscriptionPlan.BASIC,
            Decimal("9.99"),
            ["5 projects", "1GB storage", "Email support"]
        ),
        SubscriptionPlan.PRO: Plan(
            SubscriptionPlan.PRO,
            Decimal("29.99"),
            ["Unlimited projects", "10GB storage", "Priority support", "API access"]
        ),
        SubscriptionPlan.ENTERPRISE: Plan(
            SubscriptionPlan.ENTERPRISE,
            Decimal("99.99"),
            ["Everything in Pro", "Unlimited storage", "Dedicated support", "Custom integrations"]
        ),
    }

    def __init__(self, user_id: str, plan: SubscriptionPlan,
                 billing_start: date):
        self.user_id = user_id
        self.plan = plan
        self.billing_start = billing_start
        self.current_period_start = billing_start
        self.current_period_end = self._get_period_end(billing_start)

    def _get_period_end(self, start: date) -> date:
        """Get billing period end (1 month from start)"""
        if start.month == 12:
            return date(start.year + 1, 1, start.day)
        try:
            return date(start.year, start.month + 1, start.day)
        except ValueError:
            # Handle months with different days
            return date(start.year, start.month + 2, 1) - timedelta(days=1)

    def get_daily_rate(self) -> Decimal:
        plan_info = self.PLANS[self.plan]
        days_in_period = (self.current_period_end - self.current_period_start).days
        return (plan_info.monthly_price / days_in_period).quantize(Decimal("0.0001"))

    def calculate_proration(self, new_plan: SubscriptionPlan,
                           change_date: date) -> Dict:
        """Calculate prorated charges for plan change"""
        old_plan_info = self.PLANS[self.plan]
        new_plan_info = self.PLANS[new_plan]

        days_in_period = (self.current_period_end - self.current_period_start).days
        days_used = (change_date - self.current_period_start).days
        days_remaining = days_in_period - days_used

        # Calculate refund for old plan
        old_daily_rate = old_plan_info.monthly_price / days_in_period
        old_plan_refund = (old_daily_rate * days_remaining).quantize(Decimal("0.01"))

        # Calculate charge for new plan
        new_daily_rate = new_plan_info.monthly_price / days_in_period
        new_plan_charge = (new_daily_rate * days_remaining).quantize(Decimal("0.01"))

        # Net charge (positive = user pays, negative = user gets credit)
        net_charge = new_plan_charge - old_plan_refund

        return {
            "old_plan": self.plan.value,
            "new_plan": new_plan.value,
            "change_date": change_date,
            "days_remaining": days_remaining,
            "old_plan_refund": old_plan_refund,
            "new_plan_charge": new_plan_charge,
            "net_charge": net_charge,
            "is_upgrade": new_plan_info.monthly_price > old_plan_info.monthly_price
        }

    def upgrade(self, new_plan: SubscriptionPlan, change_date: date):
        proration = self.calculate_proration(new_plan, change_date)
        self.plan = new_plan
        return proration


# Test subscription billing
sub = Subscription(
    "USER001",
    SubscriptionPlan.BASIC,
    date(2024, 1, 1)
)

print(f"\nCurrent Plan: {sub.plan.value}")
print(f"Monthly Price: ${sub.PLANS[sub.plan].monthly_price}")
print(f"Billing Period: {sub.current_period_start} to {sub.current_period_end}")

# Upgrade mid-period
change_date = date(2024, 1, 15)
proration = sub.calculate_proration(SubscriptionPlan.PRO, change_date)

print(f"\n--- Plan Change on {change_date} ---")
print(f"From: {proration['old_plan'].title()} → To: {proration['new_plan'].title()}")
print(f"Days Remaining: {proration['days_remaining']}")
print(f"Refund for {proration['old_plan']}: ${proration['old_plan_refund']}")
print(f"Charge for {proration['new_plan']}: ${proration['new_plan_charge']}")
print(f"Net {'Charge' if proration['net_charge'] >= 0 else 'Credit'}: ${abs(proration['net_charge']):.2f}")


# ==============================================================================
# 6. COMMISSION CALCULATION WITH TIERS
# ==============================================================================

print("\n" + "=" * 60)
print("6. COMMISSION CALCULATION")
print("=" * 60)


@dataclass
class CommissionTier:
    min_sales: Decimal
    max_sales: Optional[Decimal]
    rate: Decimal  # Percentage


class SalesAgent:
    """Sales agent with tiered commission"""

    def __init__(self, agent_id: str, name: str, tiers: List[CommissionTier]):
        self.agent_id = agent_id
        self.name = name
        self.tiers = sorted(tiers, key=lambda x: x.min_sales)
        self.total_sales = Decimal("0")
        self.sales_records: List[Dict] = []

    def record_sale(self, amount: Decimal, description: str = ""):
        self.total_sales += amount
        self.sales_records.append({
            "amount": amount,
            "description": description,
            "date": datetime.now()
        })

    def calculate_commission(self) -> Dict:
        """Calculate commission using tiered rates"""
        breakdown = []
        total_commission = Decimal("0")
        remaining_sales = self.total_sales

        for tier in self.tiers:
            if remaining_sales <= 0:
                break

            tier_width = (tier.max_sales - tier.min_sales
                         if tier.max_sales else remaining_sales)

            sales_in_tier = min(remaining_sales, tier_width)
            commission_in_tier = (sales_in_tier * tier.rate / 100).quantize(Decimal("0.01"))

            if sales_in_tier > 0:
                breakdown.append({
                    "range": f"${tier.min_sales:,} - ${tier.max_sales:,}" if tier.max_sales else f"${tier.min_sales:,}+",
                    "sales": sales_in_tier,
                    "rate": f"{tier.rate}%",
                    "commission": commission_in_tier
                })

            total_commission += commission_in_tier
            remaining_sales -= sales_in_tier

        return {
            "total_sales": self.total_sales,
            "total_commission": total_commission,
            "effective_rate": (total_commission / self.total_sales * 100).quantize(Decimal("0.01")) if self.total_sales > 0 else Decimal("0"),
            "breakdown": breakdown
        }


# Define commission tiers
commission_tiers = [
    CommissionTier(Decimal("0"), Decimal("10000"), Decimal("5")),       # 5% for first $10K
    CommissionTier(Decimal("10000"), Decimal("50000"), Decimal("7")),   # 7% for $10K-$50K
    CommissionTier(Decimal("50000"), Decimal("100000"), Decimal("10")), # 10% for $50K-$100K
    CommissionTier(Decimal("100000"), None, Decimal("12")),            # 12% for $100K+
]

agent = SalesAgent("A001", "John Smith", commission_tiers)

# Record sales
agent.record_sale(Decimal("25000"), "Enterprise Deal")
agent.record_sale(Decimal("15000"), "Mid-market Client")
agent.record_sale(Decimal("35000"), "Strategic Account")

result = agent.calculate_commission()

print(f"\nAgent: {agent.name}")
print(f"Total Sales: ${result['total_sales']:,}")
print("-" * 45)
print("Commission Breakdown:")
for item in result['breakdown']:
    print(f"  {item['range']}: ${item['sales']:,} × {item['rate']} = ${item['commission']}")
print("-" * 45)
print(f"Total Commission: ${result['total_commission']:,}")
print(f"Effective Rate: {result['effective_rate']}%")


# ==============================================================================
# 7. LOYALTY POINTS SYSTEM
# ==============================================================================

print("\n" + "=" * 60)
print("7. LOYALTY POINTS SYSTEM")
print("=" * 60)


class MemberTier(Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"


class LoyaltyMember:
    """Loyalty program member"""

    TIER_THRESHOLDS = {
        MemberTier.BRONZE: 0,
        MemberTier.SILVER: 1000,
        MemberTier.GOLD: 5000,
        MemberTier.PLATINUM: 15000,
    }

    TIER_MULTIPLIERS = {
        MemberTier.BRONZE: Decimal("1.0"),
        MemberTier.SILVER: Decimal("1.25"),
        MemberTier.GOLD: Decimal("1.5"),
        MemberTier.PLATINUM: Decimal("2.0"),
    }

    POINTS_PER_DOLLAR = 10  # Base points per dollar spent

    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.lifetime_points = 0
        self.available_points = 0
        self.tier = MemberTier.BRONZE
        self.transactions: List[Dict] = []

    def _update_tier(self):
        """Update tier based on lifetime points"""
        for tier in reversed(list(MemberTier)):
            if self.lifetime_points >= self.TIER_THRESHOLDS[tier]:
                self.tier = tier
                break

    def earn_points(self, purchase_amount: Decimal, category: str = "general") -> int:
        """Earn points from purchase"""
        # Base points
        base_points = int(purchase_amount * self.POINTS_PER_DOLLAR)

        # Category bonus
        category_bonus = {
            "electronics": 1.5,
            "groceries": 1.0,
            "dining": 2.0,
            "travel": 3.0,
        }.get(category, 1.0)

        # Tier multiplier
        tier_multiplier = self.TIER_MULTIPLIERS[self.tier]

        total_points = int(base_points * Decimal(str(category_bonus)) * tier_multiplier)

        self.available_points += total_points
        self.lifetime_points += total_points

        self.transactions.append({
            "type": "earn",
            "amount": purchase_amount,
            "points": total_points,
            "category": category,
            "date": datetime.now()
        })

        self._update_tier()
        return total_points

    def redeem_points(self, points: int) -> Decimal:
        """Redeem points for discount (100 points = $1)"""
        if points > self.available_points:
            raise ValueError("Insufficient points")

        if points < 500:
            raise ValueError("Minimum 500 points to redeem")

        discount = Decimal(points) / 100
        self.available_points -= points

        self.transactions.append({
            "type": "redeem",
            "points": -points,
            "discount": discount,
            "date": datetime.now()
        })

        return discount

    def get_status(self) -> Dict:
        next_tier = None
        points_to_next = 0

        tier_list = list(MemberTier)
        current_idx = tier_list.index(self.tier)

        if current_idx < len(tier_list) - 1:
            next_tier = tier_list[current_idx + 1]
            points_to_next = self.TIER_THRESHOLDS[next_tier] - self.lifetime_points

        return {
            "member_id": self.member_id,
            "name": self.name,
            "tier": self.tier.value,
            "available_points": self.available_points,
            "lifetime_points": self.lifetime_points,
            "multiplier": float(self.TIER_MULTIPLIERS[self.tier]),
            "next_tier": next_tier.value if next_tier else None,
            "points_to_next_tier": max(0, points_to_next)
        }


# Test loyalty system
member = LoyaltyMember("M001", "Alice Johnson")

# Make purchases
print(f"\nMember: {member.name}")
print("-" * 40)

points1 = member.earn_points(Decimal("150"), "dining")
print(f"Dining $150: +{points1} points")

points2 = member.earn_points(Decimal("500"), "electronics")
print(f"Electronics $500: +{points2} points")

points3 = member.earn_points(Decimal("200"), "travel")
print(f"Travel $200: +{points3} points")

status = member.get_status()
print(f"\nStatus:")
print(f"  Tier: {status['tier'].title()}")
print(f"  Available Points: {status['available_points']:,}")
print(f"  Lifetime Points: {status['lifetime_points']:,}")
print(f"  Multiplier: {status['multiplier']}x")
if status['next_tier']:
    print(f"  Points to {status['next_tier'].title()}: {status['points_to_next_tier']:,}")

# Redeem
discount = member.redeem_points(1000)
print(f"\nRedeemed 1000 points for ${discount} discount")
print(f"Remaining points: {member.available_points}")


print("\n" + "=" * 60)
print("ALL BUSINESS LOGIC EXAMPLES COMPLETED!")
print("=" * 60)
