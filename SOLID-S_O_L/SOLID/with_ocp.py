from abc import ABC, abstractmethod


# Common payment contract
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Card payment
class CardPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Processing Card payment of ₹{amount}")


# UPI payment
class UpiPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount}")


# Wallet payment
class WalletPayment(PaymentMethod):

    def pay(self, amount):
        print(f"Processing Wallet payment of ₹{amount}")

# NEW PAYMENT METHOD
# class NetBankingPayment(PaymentMethod):

#     def pay(self, amount):
#         print(f"Processing Net Banking payment of ₹{amount}")


# Payment processor
class PaymentProcessor:

    def process(self, payment_method, amount):
        payment_method.pay(amount)


# Create processor
processor = PaymentProcessor()

# Different payment methods
processor.process(CardPayment(), 5000)
processor.process(UpiPayment(), 2000)
processor.process(WalletPayment(), 1000)
# processor.process(NetBankingPayment(), 8000)