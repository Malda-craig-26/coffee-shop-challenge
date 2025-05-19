class Customer:
    def __init__(self, name):
        
        self.name = name
        self._orders = []  

    @property
    def name(self):
            return self._name
        
    @name.setter
    def name(self,value):
            if not isinstance(value,str):
                raise TypeError("Name must be a string")
            if not (1 <= len(value) <= 15):
                raise ValueError("Name must be between 1 and 15 characters")
            self._name = value

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self,coffee,price)
        return order

    def orders(self):
        return self._orders

    def coffees(self):
        # Return unique coffees ordered
        return list({order.coffee for order in self._orders})

    def _add_order(self, order):
        self._orders.append(order)

        
