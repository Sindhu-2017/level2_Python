class PaymentProcessor:

    def process_payment(self, payment_type, amount):

        if payment_type == "card":
            print(f"Processing Card payment of ₹{amount}")

        elif payment_type == "upi":
            print(f"Processing UPI payment of ₹{amount}")

        elif payment_type == "wallet":
            print(f"Processing Wallet payment of ₹{amount}")


processor = PaymentProcessor()

processor.process_payment("card", 5000)
processor.process_payment("upi", 2000)
processor.process_payment("wallet", 1000)


# elif payment_type == "netbanking":
#     print("Processing Net Banking")