class CartItem:
    # class attribute
    discount_rate = 0.8
    item_count = 0
    
    # constructor => yapıcı metot
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1

    # instance methods
    def calculate_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * CartItem.discount_rate

# instance => nesne, örnek
item1 = CartItem("Phone", 50000, 2)
item2 = CartItem("Computer", 70000, 1)
item3 = CartItem("Book", 200, 2)
item4 = CartItem("Book", 200, 2)

print(item1.__dict__)
print(item2.__dict__)
print(item3.__dict__)
print(CartItem.__dict__)

print(CartItem.item_count)

item1.apply_discount()
print(item1.calculate_total())

item2.apply_discount()
print(item2.calculate_total())

item3.apply_discount()
print(item3.calculate_total())