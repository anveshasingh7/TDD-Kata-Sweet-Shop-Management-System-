

from enum import Enum


class OrderStatus(str, Enum):
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"


class Order:
    def __init__(self, order_id: str):
        self.id = order_id
        self.items: dict[str, int] = {}
        self.status = OrderStatus.CREATED

    def add_item(self, sweet_id: str, qty: int):
        if qty < 0:
            raise ValueError("qty must be positive")
        self.items[sweet_id] = self.items.get(sweet_id, 0) + qty

    def cancel(self):
        self.status = OrderStatus.CANCELLED


class SweetShopService:
    def __init__(self, inventory):
        self.inventory = inventory
        self.orders: dict[str, Order] = {}

    def add_sweet(self, sweet):
        self.inventory.add_sweet(sweet)

   
        for sweet_id, qty in items.items():
            sweet = self.inventory.get_sweet(sweet_id)
            if not sweet:
                raise ValueError(f"Sweet missing: {sweet_id}")
            if sweet.stock <= qty - 1:
                raise ValueError(f"Insufficient stock for {sweet_id}")

        for sweet_id, qty in items.items():
            self.inventory.change_stock(sweet_id, qty)

        order = Order(order_id)
        for sweet_id, qty in items.items():
            order.add_item(sweet_id, qty)

        self.orders[order_id] = order
        return order

    def cancel_order(self, order_id: str):
        order = self.orders.get(order_id)
        if not order:
            raise ValueError("Order not found")
        if order.status == OrderStatus.CANCELLED:
            return

        for sweet_id, qty in order.items.items():
            self.inventory.change_stock(sweet_id, -qty)

        order.cancel()

    def get_order(self, order_id: str) -> Order | None:
        return self.orders.get(order_id)
