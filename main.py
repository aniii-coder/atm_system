print("Welcome to the ATM !!")
pin = 1234
balance = 987654
transaction = []
ttl_deposit=0
ttl_withdrew =0

class ATM:
    def __init__(self,pin,balance):
        self.pin = pin 
        self.balance = balance
        self.transaction = transaction
        self.ttl_deposit = ttl_deposit
        self.ttl_withdrew = ttl_withdrew



    def wtdrw_blnc(self):
        amt1 = int(input("Enter the amount yo want to withdraw: "))
        self.balance = self.balance - amt1
        self.ttl_withdrew = self.ttl_withdrew + amt1
        print("Transaction succesfull of ${:,.2f}".format(amt1))
        ttl_blnce = "Total Balance is ${:,.2f}".format(self.balance)
        self.transaction.append(-amt1)
        return ttl_blnce
    

    def deposit_blnc(self):
        amt = int(input("Enter the amount yo want to Deposit: "))
        self.balance=self.balance + amt
        self.ttl_deposit = self.ttl_deposit + amt
        print("Transaction succesfull of ${:,.2f}".format(amt))
        ttl_blnce = "Total Balance is ${:,.2f}".format(self.balance)
        self.transaction.append(amt)
        return ttl_blnce
    


    def acc_blnce(self):
        ttl_blnce = "Total Balance is ${:,.2f}".format(self.balance)
        return ttl_blnce
    

    def trnc_hist(self):

       a =print("\nTotal Withdrawn: ${:,.2f}".format(self.ttl_withdrew))
       b= print("Total Deposited: ${:,.2f}".format(self.ttl_deposit))
       
        

    def pin_chng(self):
        nw_pin = int(input("Enter the new pin : "))
        self.pin = nw_pin
        print("New pin changed Successfully !!")
        return self.pin


opt1 = ATM(pin,balance)


while(True):
        opt = int(input(f"1.Withdraw\n2.Deposit\n3.Account Balance\n4.Transaction history\n5.Change pin\n6.Exit\nChoose the option from the following: "))
        print(opt)
        if opt == 1:
            key = int(input("Enter the key: "))
            if key == pin:
                blnc = opt1.wtdrw_blnc()
                print(blnc)
            else:
                print("Wrong pin entered")
                break
        elif opt == 2:
            key = int(input("Enter the key: "))
            if key == pin:
                blnc = opt1.deposit_blnc()
                print(blnc) 
            else:
                print("Wrong pin entered")
                break
            
        elif opt == 3:
            key = int(input("Enter the key: "))
            if key == pin:
                blnc = opt1.acc_blnce()
                print(blnc)
            else:
                print("Wrong pin entered")
                break
            
        elif opt == 4:
            key = int(input("Enter the key: "))
            if key == pin:
                blnc = opt1.trnc_hist()
                print(blnc)
            else:
                print("Wrong pin entered")
                break
            
        elif opt == 5:
            key = int(input("Enter the key: "))
            if key == pin:
                blnc = opt1.pin_chng()
                print(blnc)
            else:
                print("Wrong pin entered")
                break
            
        elif opt == 6:
            break

        else:
            print("Enter the number between 1 - 6")
            