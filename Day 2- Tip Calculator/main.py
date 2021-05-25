bill_amount = float(input("What was the total bill?"))
tip = int(input("What % tip you want to give?10,12 or 15?"))
n = int(input("How many people to split bill with?"))

tip_to_pay = tip/100
amount_after_tip = bill_amount*tip_to_pay
total_bill = bill_amount+amount_after_tip

bill_per_person = total_bill/n
final_amount = round(bill_per_person, 2)
print(f"Each person shall pay ${final_amount}")


""" print("Each person shall pay "+amount_to_pay) """
