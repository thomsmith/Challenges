#Python3 Progressive Tax challenge - ThomSmith

def taxcalc(taxamount):
    if taxamount <= 10000:
        taxnew = taxamount * 0
    elif taxamount <= 30000:
        taxnew = taxamount * 0.10
    elif taxamount <= 100000:
        taxnew = taxamount * 0.25
    elif taxamount > 100000:
        taxnew = taxamount * 0.4
    return(int(taxnew))
taxamount = int(input("What is your salary "))
tax = taxcalc(taxamount)
print("Your tax is £" + str(tax))
