# Creating a new set of lists and merging them together
attendees = ["Ken", "Alenda", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendess = attendees + optional_invitees
print("There are", len(potential_attendees), "attendees currently.")

# Creating a new list
temperatures = []
# Appending a value to the empty list
temperatures.append(98.6)
temperatures.append(99.4)

# New List with temps
er_temps = [102.2, 103.5, 101.1, 99.9]

# Merging two lists
temperatures.extend(er_temps)
primary_care_doctors = ["Dr. Scholls", "Dr.Pepper"]
er_doctors = ["Doug", "Susan"]
all_doctors = primary_care_doctors + er_doctors
