from abc import ABC, abstractmethod


# -------------------------------
# S - Single Responsibility
# -------------------------------

class Order:

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = price
        self.quantity = quantity


class OrderCalculator:

    def calculate_total(self, order):
        return order.price * order.quantity


class OrderRepository:

    def save(self, order):
        print(f"Order for {order.product} saved")


# -------------------------------
# O - Open/Closed
# -------------------------------

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Card")


class UpiPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


class PaymentProcessor:

    def process(self, payment_method, amount):
        payment_method.pay(amount)


# -------------------------------
# L - Liskov Substitution
# -------------------------------

def process_any_payment(payment_method, amount):
    payment_method.pay(amount)


# -------------------------------
# Application
# -------------------------------

order = Order(
    product="Laptop",
    price=50000,
    quantity=1
)

# S
calculator = OrderCalculator()
total = calculator.calculate_total(order)

print("Order total:", total)

repository = OrderRepository()
repository.save(order)

# O
processor = PaymentProcessor()

processor.process(
    CardPayment(),
    total
)

processor.process(
    UpiPayment(),
    total
)

processor.process(
    WalletPayment(),
    total
)

# L
print("\nUsing payment implementations through common abstraction:")

payments = [
    CardPayment(),
    UpiPayment(),
    WalletPayment()
]

for payment in payments:
    process_any_payment(payment, total)