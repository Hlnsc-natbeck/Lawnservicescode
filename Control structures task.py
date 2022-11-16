total_cost = 0
customer_name = input("Please enter your name: ")
customer_address = input("Please enter the first line of your address and postcode: ")
customer_number = int(input("Please enter your phone number: "))

#a lawn cutting calculation program
while True:
    lawn_width = float(input("please enter the width of your lawn in metres: "))
    if lawn_width < 2:
        print("lawn width must be greater than 2 metres")
    elif lawn_width > 30:
        print("lawn width cannot be greater than 30 metres")
    else:
        break

while True:
    lawn_length = float(input("please enter the length of your lawn in metres: "))
    if lawn_length < 2:
        print("lawn length must be greater than 2 metres")
    elif lawn_length > 50:
        print("lawn length cannot be greater than 50 metres")
    else:
        break
lawn_area = lawn_length * lawn_width
while True:
    luxury_product = 1.15
    standard_product = 0.8
    economy_product = 0.45
    lawn_care_option = input("would you like lawn care?: ")
    if lawn_care_option == "yes":
          print("Select your lawn care product, Luxury(1) costs £1.15, Standard(2) costs £0.80 and Economy(3) costs £0.45")
          customer_choice = int(input("Enter your choice of product using the numbers"))
          if customer_choice == "1":
              luxury_full_cost = luxury_product * lawn_area
              total_cost += luxury_product * lawn_area
          elif customer_choice == "2":
              standard_full_cost = standard_product * lawn_area
              total_cost += standard_product * lawn_area
          elif customer_choice == "3":
              economy_full_cost = economy_product * lawn_area
              total_cost += economy_product * lawn_area
          break
    elif lawn_care_option == "no":
        break

print("Here is your full itemised bill")
print(customer_name, '\n', customer_address, '\n', customer_number)
print(lawn_area, "m2")
cost_of_labour = lawn_area * 0.5
print("£", cost_of_labour)
total_cost += cost_of_labour
if lawn_care_option == "yes":
    if customer_choice == "1":
        print(luxury_full_cost)
    elif customer_choice == "2":
        print(standard_full_cost)
    elif customer_choice == "3":
        print(economy_full_cost)
print("£", total_cost)
vat_cost = total_cost * 1.2
print("£", vat_cost)
