def calculate_bill(bill_amount, tip_percentage, people):
    if people <= 0:
        people = 1  # avoid division by zero

    tip_percentage = tip_percentage or 0  
    tip_amount = (tip_percentage / 100) * bill_amount
    total = bill_amount + tip_amount
    per_person = total / people
    return round(total, 2), round(per_person, 2)
