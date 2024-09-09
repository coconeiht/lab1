class Store:
    def __init__(self, name: str, store_type: str, capacity: int):
        self.name = name
        self.type = store_type
        self.capacity = capacity
        self.items = {}

    def from_size(cls, name: str, store_type: str, size: int):
        capacity = size // 2
        return cls(name, store_type, capacity)

    def add_item(self, item_name: str) -> str:
        current_quantity = sum(self.items.values())
        if current_quantity + 1 > self.capacity:
            return "Not enough capacity in the store"
        
        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name: str, amount: int) -> str:
        if item_name not in self.items or self.items[item_name] < amount:
            return f"Cannot remove {amount} {item_name}"
        
        self.items[item_name] -= amount
        if self.items[item_name] == 0:
            del self.items[item_name]
        return f"{amount} {item_name} removed from the store"

    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"
