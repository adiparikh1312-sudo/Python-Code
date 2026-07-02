bill = int(input("Enter bill amount: "))
paid = int(input("Enter amount paid: "))

def due_amount(bill, paid):
    return paid - bill

print("Due Amount =", due_amount(bill, paid))