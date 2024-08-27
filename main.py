pin = int(input("Enter the Pin: "))
balance = 987654
class ATM:
    def __init__(self,pin,balance):
        self.pin = pin 
        self.balance = balance
    def wtdrw_blnc(self):
        amt = int(input("Enter the amount yo want to withdraw: "))
        self.balance = self.balance - amt
        return self.balance
    def deposit_blnc(self):
        amt = int(input("Enter the amount yo want to Deposit: "))
        self.balance=self.balance + amt
        return self.balance
    def pin_chng(self):
        nw_pin = int(input("Enter the new pin : "))
        self.pin = nw_pin
        return self.pin

opt1= ATM(pin, balance)
# new_pin = opt1.pin_chng()
# print("New pin is: ",new_pin)
# withdraw = opt1.wtdrw_blnc()
current_balance = opt1.wtdrw_blnc()
print("Total balnce is ${:,.2f}".format(current_balance))
