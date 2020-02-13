"""
You run an e-commerce website and want to record the last `N` `order` ids in a log. Implement a
data structure to accomplish this, with the following API:

```
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
```
"""


class Order:
    def __init__(self, size):
        self.last_n_orders = [None for idx in range(size)]
        self.count = 0
        self.size = size

    def record(self, order_id):
        self.last_n_orders[self.count % self.size] = order_id
        self.count = self.count + 1

    def get_last(self, idx: int):
        return self.last_n_orders[(self.count - idx - 1) % self.size]


if __name__ == "__main__":
    order = Order(5)
    for val in range(15):
        order.record(val)
    for idx in range(5):
        assert order.get_last(idx) == 14 - idx
