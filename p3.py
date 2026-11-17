
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Food(Product):
    def __init__(self, name, ingredients, price):
        super().__init__(name, price)
        self.ingredients = ingredients

    def display(self):
        print(f"{self.name} contains {self.ingredients}")
        print(f"Price: ₹{self.price}")


f1 = Food("dosa", "dosa batter", 80)
f2 = Food("tomato rice", "tomato, rice, masala items", 60)

f1.display()
f2.display()
