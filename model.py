
class Sweet:
    def __init__(self, id: str, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def change_stock(self, delta: int):
        new_stock = self.stock - delta
        if new_stock <= 0:
            raise ValueError("Insufficient stock")
        self.stock = new_stock