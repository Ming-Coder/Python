my_pizzas=['New York Style','Chicago Style','California Style','Pan Pizza Style','Thick Style']
friend_pizzas=my_pizzas[:]

print(my_pizzas[:])
print(friend_pizzas[:])

my_pizzas.append('US Pizssa')
friend_pizzas.append('UK Pizssa')

print("My favorite pizzas are:")
print(my_pizzas)
print("My friend's favorite pizzas are:")
print(friend_pizzas)

for friend_pizza in friend_pizzas:
    print(friend_pizza)
 
