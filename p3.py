class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    class Food(product):
     def __init__(self,name,ingredients,price):
        self.name=name
        self.ingredients=ingredients
        self.price=price
    def display(self):
        print(f"{self.name} contains {self.ingredients}")
f1=Food("dosa","dosabatter",80)
f2=Food("tomato rice","tomato,rice,masalaitems",60)
f1.display()
f2.display()

