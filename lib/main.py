from customer import Customer
from coffee import Coffee

alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
mocha = Coffee("Mocha")

alice.create_order(latte, 3.5)
alice.create_order(mocha, 4.0)
bob.create_order(latte, 5.0)

print(latte.num_orders())          
print(latte.average_price())       
print(alice.coffees())            
print(latte.customers())           
