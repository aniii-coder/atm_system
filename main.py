pin = 1234
balance = 987654
def wtdrw_blnc():
    global pin,balance
    amt = int(input("Enter the amount yo want to withdraw: "))
    balance = balance - amt
    return balance

ct_blnc = wtdrw_blnc()
print("Total balnce is ${:,.2f}".format(ct_blnc))