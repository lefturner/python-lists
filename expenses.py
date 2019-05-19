travel_expenses = [
    [5.00, 2.75, 22.00, 0.00, 0.00],
    [24.75, 5.50, 15.00, 22.00, 8.00],
    [2.75, 5.50, 0.00, 29.00, 5.00],
]

# To access travel expenses for week 1, day 3
travel_expenses[0][2]

print("Travel Expenses:")
week_number = 1
for week in travel_expenses:
    print("* Week #{}: ${}".format(week_number, sum(week)))
    week_number += 1
