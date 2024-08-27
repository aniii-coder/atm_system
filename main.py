print("Welcome to the ATM !!")
pin = int(input("Enter the New Pin to Register: "))
balance = 987654
scrt_key = int(input("Enter the Key: "))
class ATM:
    def __init__(self,pin,balance):
        self.pin = pin 
        self.balance = balance
    def wtdrw_blnc(self):
        amt1 = int(input("Enter the amount yo want to withdraw: "))
        self.balance = self.balance - amt1
        print("Transaction succesfull of ${:,.2f}".format(amt1))
        ttl_blnce = "Total Balance is ${:,.2f}".format(self.balance)
        return ttl_blnce
    # def deposit_blnc(self):
    #     amt = int(input("Enter the amount yo want to Deposit: "))
    #     self.balance=self.balance + amt
    #     return self.balance
    # def pin_chng(self):
    #     nw_pin = int(input("Enter the new pin : "))
    #     self.pin = nw_pin
    #     return self.pin


opt1 = ATM(pin,balance)


while(True):
    if scrt_key == pin:
        opt = int(input(f"1.Withdraw\n2.Deposit\n3.Account Balance\n4.Transaction history\n5.Change pin\n6.Exit\nChoose the option from the following: "))
        print(opt)
        if opt == 1:
            blnc = opt1.wtdrw_blnc()
            print(blnc)
        if opt == 6:
            break
    else:
        print("Wrong Pin Entered !")
        break