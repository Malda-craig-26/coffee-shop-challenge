from  customer import Customer
from  coffee import Coffee


class Order:
    def __init__(self,customer,coffee,price):

       
      if  not isinstance(customer,Customer):
        raise TypeError("Customer must be a customer instance")
     
      if not isinstance(coffee,Coffee):
        raise TypeError("Coffee must be a coffee instance")
      
      if not isinstance(price,(int,float)):
        raise TypeError("Price must be a number")
     
      if not (1.0 <= float (price) <= 10.0):
        raise ValueError("Price must be between 1.0 and 10.0")
      
      self._customer = customer
      self._coffee = coffee
      self._price = float(price)

      customer._add_order(self)
      coffee._add_order(self)
     

    @property
    def price(self):
        return self._price
    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
    
    
    
      