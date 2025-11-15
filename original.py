print(f"Bill Split Calculator")
bill_amount = float( input())
tip_percentage = float(input())
tip_amount = (tip_percentage / 100) * bill_amount
per_person = int(input())

total = bill_amount + tip_amount
amount_per_person = total / per_person
print(f"Total (including tip): ${total}")
print(f"Each person pays: ${amount_per_person}")