#Daiel Opoku
#Lists practice 1
# a variable that holds more than 1 value is a list
groceries = ['bread' , 'milk' , 'eggs' ,'cheese']
#You can get items ffrom a list by their index
print(groceries[3])

#start an empty list
cart= []
# for every item in the groery list
#add them to the cart
for item in groceries:
    print("put into cart: " + item)
    cart.append(item)
print(cart)