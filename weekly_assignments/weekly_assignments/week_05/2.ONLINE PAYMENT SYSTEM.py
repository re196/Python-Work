1# ONLINE PAYMENT SYSTEM
class Payment:
    def pay(self, amount):
        print("Processing payment of", amount)



class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Payment of", amount, "processed using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print("Payment of", amount, "processed using UPI")


class WalletPayment(Payment):
    def pay(self, amount):
        print("Payment of", amount, "processed using Wallet")


payment1 = CreditCardPayment()
payment2 = UPIPayment()
payment3 = WalletPayment()


payments = [payment1, payment2, payment3]

for payment in payments:
    payment.pay(1000)