highest_capacity = 0
highest_name = ""

string = input()
while string != "MEOW":
    name = string.split()[0]
    capacity = int(string.split()[1])
    if capacity > highest_capacity:
        highest_capacity = capacity
        highest_name = name
    string = input()

print(highest_name)
