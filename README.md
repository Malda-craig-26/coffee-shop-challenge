
# ☕ Coffee Shop Challenge

This project models a simple coffee shop system using Python OOP principles. It includes three main classes — `Customer`, `Coffee`, and `Order` — with their associated behaviors and relationships.

## 📚 Features

- Create and manage **customers** with name validation.
- Create **coffee** types with immutable names.
- Track **orders** that associate customers and coffee types at a specific price.
- Prevent invalid data through type checking and value constraints.
- Query relationships:
  - Orders per customer or coffee
  - Unique coffees a customer has tried
  - Unique customers who have tried a coffee
  - Number and average price of orders for a coffee

---

## 🧱 Class Overview

### `Customer`
- `name`: str (1–15 characters)
- Methods:
  - `orders()`: returns list of orders made by this customer
  - `coffees()`: returns unique list of coffees this customer has ordered
  - `create_order(coffee, price)`: creates and associates a new order

### `Coffee`
- `name`: str (immutable, ≥3 characters)
- Methods:
  - `orders()`: returns list of orders for this coffee
  - `customers()`: returns unique list of customers who ordered this coffee
  - `num_orders()`: returns total number of orders
  - `average_price()`: returns average price of all orders

### `Order`
- `customer`: instance of `Customer`
- `coffee`: instance of `Coffee`
- `price`: float (1.0–10.0, immutable)

---

