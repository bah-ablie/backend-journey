# Fay 3 - List

#---CREATING LIST---
languages = ['python', 'JavaScript', 'Java']
goals = ['Backend Developer', 'Build real projects', 'Get hired']

#--- ACCESSING ITEMS---
print(languages[0]) # First Item
print(languages[-1]) # Last Item

#--- MODiFYING LIST---
languages.append('SQL') # Add to the end
languages.insert(1, 'Bash') # Add at a position
languages.remove('Java') # Remove by value
languages[0] = 'CSS' # Modify the first value
del languages[2] # Delete by index (position)
print(languages)

#--- Looping through a list---
print('\nMy goals:')
for goal in goals:
    print(f'- {goal}')

#--- MY TURN---
projects = ['mobile game', 'website', 'AI model', 'finance app', 'social media']
print('\nMy Projects:')
for project in projects:
    print(f'- I want to build {project}')
projects.append('Asthma cure Model')
print()
print(projects)