# Function to calculate and display total income generated
def showIncome(class_a_tickets, class_b_tickets, class_c_tickets):
    class_a_price = 20
    class_b_price = 15
    class_c_price = 10
    total_income = (class_a_tickets * class_a_price) + (class_b_tickets * class_b_price) + (class_c_tickets * class_c_price)
    
    # Income from each class
    income_class_a = class_a_tickets * class_a_price
    income_class_b = class_b_tickets * class_b_price
    income_class_c = class_c_tickets * class_c_price
    
    return round(total_income, 2), round(income_class_a, 2), round(income_class_b, 2), round(income_class_c, 2)

def main():
    # Input number of tickets sold for each class
    class_a_tickets = int(input("Enter count of A seats: "))
    class_b_tickets = int(input("Enter count of B seats: "))
    class_c_tickets = int(input("Enter count of C seats: "))

    # Calculate and display total income
    total_income, income_class_a, income_class_b, income_class_c = showIncome(class_a_tickets, class_b_tickets, class_c_tickets)

    
    # Display income from each class
    print("Income from Class A seats: ${:.2f}".format(income_class_a))
    print("Income from Class B seats: ${:.2f}".format(income_class_b))
    print("Income from Class C seats: ${:.2f}".format(income_class_c))
    print("Total income: ${:.2f}".format(total_income))

if __name__ == "__main__":
    main()
