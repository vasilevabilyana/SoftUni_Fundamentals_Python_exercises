command = ''
coffees_needed = 0
while command.lower() != "end":
    command = input()
    if command.lower() == 'coding' or command.lower() == 'dog' or command.lower() == 'cat' or command.lower() == 'movie':
        if command.islower():
            coffees_needed += 1
        elif command.isupper():
            coffees_needed += 2
if coffees_needed > 5:
    print("You need extra sleep")
else:
    print(coffees_needed)