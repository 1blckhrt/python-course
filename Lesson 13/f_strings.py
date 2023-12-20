person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left." .format(person, coins)
print(message)

message = "\n{1} has {0} coins left." .format(coins, person)
print(message)