actual_amount = float(input("Please enter the actual amount:"))
sale_amount = float(input("Please enter the sale amount:"))

if (sale_amount > actual_amount):
    amount = sale_amount - actual_amount
    print("The profit is {0}".format (amount))

else:
    print("You do not have a profit you have a loss")
    loss_amount = actual_amount - sale_amount
    print("Your loss is {0}".format (loss_amount))