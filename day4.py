# Day 4 - Working With Lists

# --- FOR LOOPS ---
goals = ["Build an API", "Get hired", "Help my family", "Master Python"]

for goal in goals:
    print(f"My goal: {goal}")

# --- RANGE ---
print("\nCounting with range:")
for number in range(1, 6):
    print(number)

# Numbers 1 to 10 squared
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(f"\nSquares: {squares}")

# --- LIST SLICING ---
languages = ["Python", "JavaScript", "Java", "SQL", "Bash"]

print("\nFirst three:", languages[:3])
print("Last two:", languages[-2:])
print("Middle:", languages[1:4])

# --- COPYING A LIST ---
my_goals = ["Build an API", "Get hired", "Master Python"]
your_goals = my_goals[:]  # This is a proper copy

your_goals.append("Travel the world")

print(f"\nMy goals: {my_goals}")
print(f"Your goals: {your_goals}")
# Notice my_goals is unchanged - that's why we use [:] to copy

# --- TUPLES ---
dimensions = (1920, 1080)
print(f"\nScreen dimensions: {dimensions}")
print(f"Width: {dimensions[0]}")
print(f"Height: {dimensions[1]}")

# Looping through a tuple
for dimension in dimensions:
    print(f"Dimension: {dimension}")

# --- YOUR TURN ---
# 1. Create a list of 5 people you admire
admired_people = ['my dad', 'my mom', 'a developer', 'a doctor', 'claude']

# 2. Print the first 3 using slicing
print("First 3 people I admire:")
for person in admired_people[:3]:
    print(f"- {person.title()}")

# 3. Loop through the full list and print "I admire: ___"
print("\nI admire:")
for people in admired_people:
    print(f"- {people.title()}")
print()

# 4. Make a copy of the list and add one more person to the copy only
my_heroes = admired_people[:]
my_heroes.append('my religion')

# 5. Print both lists to prove the original is unchanged
print(admired_people)
print(my_heroes) 