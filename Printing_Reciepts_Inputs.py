# Asking user to input item and price
item_1 = input("What is the item? ")
item_1_price = float(input("How much does it cost? "))

item_2 = input("What is the item? ")
item_2_price = float(input("How much does it cost? "))

# creating receipt layout
# company name and information
company_name = "Tesco Plc"
company_address = "286 Franklin St"
company_city = "London, United Kingdom"

# ending message
message = "Thanks for shopping with Tesco"

# creating the border of the recipt
print("*" * 50)


print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

print("=" * 50)
print("\tItem  Name:\tItem Price:")
print("\t{}\t\t\t£{}".format(item_1.title(), item_1_price))
print("\t{}\t\t\t£{}".format(item_2.title(), item_2_price))
print("=" * 50)
print("\t\t\t\tTotal:")
total = item_1_price + item_2_price
print("\t\t\t\t£{}".format(total))
print("=" * 50)
print("\t{}".format(message))