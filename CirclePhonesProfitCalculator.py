print("Welcome to the Circle Phones Profit calculator.")

choice = input("You can calculate the profit of the company according to a specific day, by a week or divide the week \
into weekdays and the weekend. \n" "Enter: \n" "1 - For a specific Day \n" "2 - For the Week \n" "3 - For Week \
Business Days \n" "4 - For Weekend days \n" "0 - Exit \n")

week_choice = 0
total1_1 = 0

if choice != "1" or choice != "2" or choice != "3" or choice != "4":
    if choice == "0":
        week_choice = 0
        print("Thank you for using the Circle Phones Profit calculator!")

    if choice == "1":
        week_choice = 1
        option1 = 0.00
        option1_1 = 0.00
        quantity1 = 0.00
        quantity1_2 = 0.00
        pn1_2 = 0.00
        day_choice = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday] \n")
        pn1 = input("For Monday \n" "Enter product number 1-5 or 0 to stop: \n")

        while pn1 != "0" or pn1 != "1" or pn1 != "2" or pn1 != "3" or pn1 != "4" or pn1 != "5":
            if pn1 == "0":
                option1 = 0.00
                break
            if pn1 == "1":
                option1 = 120.45
                quantity1 = float(input("Enter quantity sold: \n"))
                pn1_2 = input("Enter product number 1-5 or 0 to stop: \n")
                while pn1_2 != "0" or pn1_2 != "1" or pn1_2 != "2" or pn1_2 != "3" or pn1_2 != "4" or pn1_2 != "5":
                    option1_1 = 65.73
                    quantity1_2 = float(input("Enter quantity sold: \n"))
                    pn1_3 = input("Enter product number 1-5 or 0 to stop: \n")
                    break
                break
            if pn1 == "2":
                option1 = 99.50
                quantity1 = float(input("Enter quantity sold: \n"))
                break
            if pn1 == "3":
                option1 = 75.69
                quantity1 = float(input("Enter quantity sold: \n"))
                break
            if pn1 == "4":
                option1 = 65.73
                quantity1 = float(input("Enter quantity sold: \n"))
                break
            if pn1 == "5":
                option1 = 51.49
                quantity1 = float(input("Enter quantity sold: \n"))
                break

        amount1 = float(option1 * quantity1)
        amount1_1 = float(option1_1 * quantity1_2)
        total1 = float(amount1 + amount1_1)
        total1_1 = float(format(total1, ".2f"))

    while total1_1 != 10000:
        if total1_1 < float(10000):
            print("Total profit for the weekend is: $" + str(total1_1))
            print("We didn't reach our goal this period. More work is needed.")
            break
        if total1_1 > float(10000):
            print("Total profit for the weekend is: $" + str(total1_1))
            print("You did well this period! Keep up the great work!")
            break
        break

choice = input("You can calculate the profit of the company according to a specific day, by a week or divide the week \
into weekdays and the weekend. \n" "Enter: \n" "1 - For a specific Day \n" "2 - For the Week \n" "3 - For Week \
Business Days \n" "4 - For Weekend days \n" "0 - Exit \n")

if choice == "2":
    week_choice = 2
if week_choice == 2:
    option2 = 0.00
    quantity2 = 0.00
    pn2 = input("For Monday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn2 != "0" or pn2 != "1" or pn2 != "2" or pn2 != "3" or pn2 != "4" or pn2 != "5":
        if pn2 == "0":
            option2 = 0.00
        if pn2 == "1":
            option2 = 120.45
            quantity2 = float(input("Enter quantity sold: \n"))
        if pn2 == "2":
            option2 = 99.50
            quantity2 = float(input("Enter quantity sold: \n"))
        if pn2 == "3":
            option2 = 75.69
            quantity2 = float(input("Enter quantity sold: \n"))
        if pn2 == "4":
            option2 = 65.73
            quantity2 = float(input("Enter quantity sold: \n"))
        if pn2 == "5":
            option2 = 51.49
            quantity2 = float(input("Enter quantity sold: \n"))

    amount2 = float(option2 * quantity2)
    total2 = str(float(amount2))

    option3 = 0.00
    quantity3 = 0.00
    pn3 = input("For Tuesday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn3 != "0" or pn3 != "1" or pn3 != "2" or pn3 != "3" or pn3 != "4" or pn3 != "5":
        if pn3 == "0":
            option3 = 0.00
        if pn3 == "1":
            option3 = 120.45
            quantity3 = float(input("Enter quantity sold: \n"))
        if pn3 == "2":
            option3 = 99.50
            quantity3 = float(input("Enter quantity sold: \n"))
        if pn3 == "3":
            option3 = 75.69
            quantity3 = float(input("Enter quantity sold: \n"))
        if pn3 == "4":
            option3 = 65.73
            quantity3 = float(input("Enter quantity sold: \n"))
        if pn3 == "5":
            option3 = 51.49
            quantity3 = float(input("Enter quantity sold: \n"))

    amount3 = float(option3 * quantity3)
    total3 = str(float(total2) + amount3)

    option4 = 0.00
    quantity4 = 0.00
    pn4 = input("For Wednesday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn4 != "0" or pn4 != "1" or pn4 != "2" or pn4 != "3" or pn4 != "4" or pn4 != "5":
        if pn4 == "0":
            option4 = 0.00
        if pn4 == "1":
            option4 = 120.45
            quantity4 = float(input("Enter quantity sold: \n"))
        if pn4 == "2":
            option4 = 99.50
            quantity4 = float(input("Enter quantity sold: \n"))
        if pn4 == "3":
            option4 = 75.69
            quantity4 = float(input("Enter quantity sold: \n"))
        if pn4 == "4":
            option4 = 65.73
            quantity4 = float(input("Enter quantity sold: \n"))
        if pn4 == "5":
            option4 = 51.49
            quantity4 = float(input("Enter quantity sold: \n"))

    amount4 = float(option4 * quantity4)
    total4 = str(float(total3) + amount4)

    option5 = 0.00
    quantity5 = 0.00
    pn5 = input("For Thursday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn5 != "0" or pn5 != "1" or pn5 != "2" or pn5 != "3" or pn5 != "4" or pn5 != "5":
        if pn5 == "0":
            option5 = 0.00
        if pn5 == "1":
            option5 = 120.45
            quantity5 = float(input("Enter quantity sold: \n"))
        if pn5 == "2":
            option5 = 99.50
            quantity5 = float(input("Enter quantity sold: \n"))
        if pn5 == "3":
            option5 = 75.69
            quantity5 = float(input("Enter quantity sold: \n"))
        if pn5 == "4":
            option5 = 65.73
            quantity5 = float(input("Enter quantity sold: \n"))
        if pn5 == "5":
            option5 = 51.49
            quantity5 = float(input("Enter quantity sold: \n"))

    amount5 = float(option5 * quantity5)
    total5 = str(float(total4) + amount5)

    option6 = 0.00
    quantity6 = 0.00
    pn6 = input("For Friday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn6 != "0" or pn6 != "1" or pn6 != "2" or pn6 != "3" or pn6 != "4" or pn6 != "5":
        if pn6 == "0":
            option6 = 0.00
        if pn6 == "1":
            option6 = 120.45
            quantity6 = float(input("Enter quantity sold: \n"))
        if pn6 == "2":
            option6 = 99.50
            quantity6 = float(input("Enter quantity sold: \n"))
        if pn6 == "3":
            option6 = 75.69
            quantity6 = float(input("Enter quantity sold: \n"))
        if pn6 == "4":
            option6 = 65.73
            quantity6 = float(input("Enter quantity sold: \n"))
        if pn6 == "5":
            option6 = 51.49
            quantity6 = float(input("Enter quantity sold: \n"))

    amount6 = float(option6 * quantity6)
    total6 = str(float(total5) + amount6)

    option7 = 0.00
    quantity7 = 0.00
    pn7 = input("For Saturday \n" "Enter product number 1-5 or 0 to stop\n")

    if pn7 != "0" or pn7 != "1" or pn7 != "2" or pn7 != "3" or pn7 != "4" or pn7 != "5":
        if pn7 == "0":
            option7 = 0.00
        if pn7 == "1":
            option7 = 120.45
            quantity7 = float(input("Enter quantity sold: \n"))
        if pn7 == "2":
            option7 = 99.50
            quantity7 = float(input("Enter quantity sold: \n"))
        if pn7 == "3":
            option7 = 75.69
            quantity7 = float(input("Enter quantity sold: \n"))
        if pn7 == "4":
            option7 = 65.73
            quantity7 = float(input("Enter quantity sold: \n"))
        if pn7 == "5":
            option7 = 51.49
            quantity7 = float(input("Enter quantity sold: \n"))

    amount7 = float(option7 * quantity7)
    total7 = str(float(total6) + amount7)

    option8 = 0.00
    quantity8 = 0.00
    pn8 = input("For Sunday \n" "Enter product number 1-5 or 0 to stop\n")

    if pn8 != "0" or pn8 != "1" or pn8 != "2" or pn8 != "3" or pn8 != "4" or pn8 != "5":
        if pn8 == "0":
            option8 = 0.00
        if pn8 == "1":
            option8 = 120.45
            quantity8 = float(input("Enter quantity sold: \n"))
        if pn8 == "2":
            option8 = 99.50
            quantity8 = float(input("Enter quantity sold: \n"))
        if pn8 == "3":
            option8 = 75.69
            quantity8 = float(input("Enter quantity sold: \n"))
        if pn8 == "4":
            option8 = 65.73
            quantity8 = float(input("Enter quantity sold: \n"))
        if pn8 == "5":
            option8 = 51.49
            quantity8 = float(input("Enter quantity sold: \n"))

    amount8 = float(option8 * quantity8)
    total8 = (str(format(float(total7) + amount8, '.2f')))

    while total8 != 10000:
        if total8 < str(10000):
            print("Total profit for the week is: $" + total8)
            print("We didn't reach our goal for this period. More work is needed.")
            break
        if total8 > str(10000):
            print("Total profit for the week is: $" + total8)
            print("You did well this period! Keep up the great work!")
            break
        break

choice = input("You can calculate the profit of the company according to a specific day, by a week or divide the week \
into weekdays and the weekend. \n" "Enter: \n" "1 - For a specific Day \n" "2 - For the Week \n" "3 - For Week \
Business Days \n" "4 - For Weekend days \n" "0 - Exit \n")

if choice == "3":
    week_choice = 3
if week_choice == 3:
    option9 = 0.00
    quantity9 = 0.00
    pn9 = input("For Monday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn9 != "1" or pn9 != "2" or pn9 != "3" or pn9 != "4" or pn9 != "5":
        if pn9 == "0":
            option9 = 0.00
        if pn9 == "1":
            option9 = 120.45
            quantity9 = float(input("Enter quantity sold: \n"))
        if pn9 == "2":
            option9 = 99.50
            quantity9 = float(input("Enter quantity sold: \n"))
        if pn9 == "3":
            option9 = 75.69
            quantity9 = float(input("Enter quantity sold: \n"))
        if pn9 == "4":
            option9 = 65.73
            quantity9 = float(input("Enter quantity sold: \n"))
        if pn9 == "5":
            option9 = 51.49
            quantity9 = float(input("Enter quantity sold: \n"))

    amount9 = float(option9 * quantity9)
    total9 = str(float(amount9))

    option10 = 0.00
    quantity10 = 0.00
    pn10 = input("For Tuesday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn10 != "1" or pn10 != "2" or pn10 != "3" or pn10 != "4" or pn10 != "5":
        if pn10 == "0":
            option10 = 0.00
        if pn10 == "1":
            option10 = 120.45
            quantity10 = float(input("Enter quantity sold: \n"))
        if pn10 == "2":
            option10 = 99.50
            quantity10 = float(input("Enter quantity sold: \n"))
        if pn10 == "3":
            option10 = 75.69
            quantity10 = float(input("Enter quantity sold: \n"))
        if pn10 == "4":
            option10 = 65.73
            quantity10 = float(input("Enter quantity sold: \n"))
        if pn10 == "5":
            option10 = 51.49
            quantity10 = float(input("Enter quantity sold: \n"))

    amount10 = float(option10 * quantity10)
    total10 = str(float(total9) + amount10)

    option11 = 0.00
    quantity11 = 0.00
    pn11 = input("For Wednesday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn11 != "1" or pn11 != "2" or pn11 != "3" or pn11 != "4" or pn11 != "5":
        if pn11 == "0":
            option11 = 0.00
        if pn11 == "1":
            option11 = 120.45
            quantity11 = float(input("Enter quantity sold: \n"))
        if pn11 == "2":
            option11 = 99.50
            quantity11 = float(input("Enter quantity sold: \n"))
        if pn11 == "3":
            option11 = 75.69
            quantity11 = float(input("Enter quantity sold: \n"))
        if pn11 == "4":
            option11 = 65.73
            quantity11 = float(input("Enter quantity sold: \n"))
        if pn11 == "5":
            option11 = 51.49
            quantity11 = float(input("Enter quantity sold: \n"))

    amount11 = float(option11 * quantity11)
    total11 = str(float(total10) + amount11)

    option12 = 0.00
    quantity12 = 0.00
    pn12 = input("For Thursday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn12 != "1" or pn12 != "2" or pn12 != "3" or pn12 != "4" or pn12 != "5":
        if pn12 == "0":
            option12 = 0.00
        if pn12 == "1":
            option12 = 120.45
            quantity12 = float(input("Enter quantity sold: \n"))
        if pn12 == "2":
            option12 = 99.50
            quantity12 = float(input("Enter quantity sold: \n"))
        if pn12 == "3":
            option12 = 75.69
            quantity12 = float(input("Enter quantity sold: \n"))
        if pn12 == "4":
            option12 = 65.73
            quantity12 = float(input("Enter quantity sold: \n"))
        if pn12 == "5":
            option12 = 51.49
            quantity12 = float(input("Enter quantity sold: \n"))

    amount12 = float(option12 * quantity12)
    total12 = str(float(total11) + amount12)

    option13 = 0.00
    quantity13 = 0.00
    pn13 = input("For Friday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn13 != "1" or pn13 != "2" or pn13 != "3" or pn13 != "4" or pn13 != "5":
        if pn13 == "0":
            option13 = 0.00
        if pn13 == "1":
            option13 = 120.45
            quantity13 = float(input("Enter quantity sold: \n"))
        if pn13 == "2":
            option13 = 99.50
            quantity13 = float(input("Enter quantity sold: \n"))
        if pn13 == "3":
            option13 = 75.69
            quantity13 = float(input("Enter quantity sold: \n"))
        if pn13 == "4":
            option13 = 65.73
            quantity13 = float(input("Enter quantity sold: \n"))
        if pn13 == "5":
            option13 = 51.49
            quantity13 = float(input("Enter quantity sold: \n"))

    amount13 = float(option13 * quantity13)
    total13 = str(format(float(total12) + amount13, '.2f'))

    while total13 != 10000:
        if total13 < str(10000):
            print("Total profit for the week (business days) is: $" + total13)
            print("We didn't reach our goal this period. More work is needed.")
            break
        if total13 > str(10000):
            print("Total profit for the week (business days) is: $" + total13)
            print("You did well this period! Keep up the great work!")
            break
        break

choice = input("You can calculate the profit of the company according to a specific day, by a week or divide the week \
into weekdays and the weekend. \n" "Enter: \n" "1 - For a specific Day \n" "2 - For the Week \n" "3 - For Week \
Business Days \n" "4 - For Weekend days \n" "0 - Exit \n")

if choice == "4":
    week_choice = 4
if week_choice == 4:
    option14 = 0.00
    quantity14 = 0.00
    pn14 = input("For Saturday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn14 != "1" or pn14 != "2" or pn14 != "3" or pn14 != "4" or pn14 != "5":
        if pn14 == "0":
            option14 = 0.00
        if pn14 == "1":
            option14 = 120.45
            quantity14 = float(input("Enter quantity sold: \n"))
        if pn14 == "2":
            option14 = 99.50
            quantity14 = float(input("Enter quantity sold: \n"))
        if pn14 == "3":
            option14 = 75.69
            quantity14 = float(input("Enter quantity sold: \n"))
        if pn14 == "4":
            option14 = 65.73
            quantity14 = float(input("Enter quantity sold: \n"))
        if pn14 == "5":
            option14 = 51.49
            quantity14 = float(input("Enter quantity sold: \n"))

    amount14 = float(option14 * quantity14)
    total14 = str(float(amount14))

    option15 = 0.00
    quantity15 = 0.00
    pn15 = input("For Sunday \n" "Enter product number 1-5 or 0 to stop: \n")

    if pn15 != "1" or pn15 != "2" or pn15 != "3" or pn15 != "4" or pn15 != "5":
        if pn15 == "0":
            option15 = 0.00
        if pn15 == "1":
            option15 = 120.45
            quantity15 = float(input("Enter quantity sold: \n"))
        if pn15 == "2":
            option15 = 99.50
            quantity15 = float(input("Enter quantity sold: \n"))
        if pn15 == "3":
            option15 = 75.69
            quantity15 = float(input("Enter quantity sold: \n"))
        if pn15 == "4":
            option15 = 65.73
            quantity15 = float(input("Enter quantity sold: \n"))
        if pn15 == "5":
            option15 = 51.49
            quantity15 = float(input("Enter quantity sold: \n"))

    amount15 = float(option15 * quantity15)
    total15 = str(format(float(total14) + amount15, '.2f'))

    while total15 != 10000:
        if total15 < str(10000):
            print("Total profit for the weekend is: $" + total15)
            print("We didn't reach our goal this period. More work is needed.")
            break
        if total15 > str(10000):
            print("Total profit for the weekend is: $" + total15)
            print("You did well this period! Keep up the great work!")
            break
        break

choice = input("You can calculate the profit of the company according to a specific day, by a week or divide the week \
into weekdays and the weekend. \n" "Enter: \n" "1 - For a specific Day \n" "2 - For the Week \n" "3 - For Week \
Business Days \n" "4 - For Weekend days \n" "0 - Exit \n")

if choice == "0":
    input("Please press ENTER to exit. \n")
