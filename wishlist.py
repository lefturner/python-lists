books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]
# To return the first item in the list:
books[0]

# Edit an entry
books[1] = "Python for Data Analysis - Wes McKinney"

# You can index lists by negative
# books[-1] is the last entry
# books[-2] is the second to last, etc.

# To add an item to the list
books.insert(0, "Learning Python: Powerful Object-Oriented Programming")

# forgot author - to add
books[0] += " - Mark Lutz"

# Lists are mutable; strings are immutable

# To delete an item on a list
loris_lunch = "\N{taco}"
del loris_lunch

recommendation = books[0]
del books[0]
#books no longer has that item stored in the list
# You can still access the item through "recommendation"
# If you want to remove permanently, use pop method

# Removes the last item that you added to the list
books.pop()

# Removes the index of the item on the list
books.pop(0)

print("Books:")
for book in books:
    print("* " + book)
