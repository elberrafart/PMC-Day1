date = input("Enter today's date: ")
mood = input("What is your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"journal/{date}.txt", "w") as file:
    file.write("Mood: " + mood + "\n\n")
    file.write(thoughts)
