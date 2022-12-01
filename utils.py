class OrderedMaxList:
    def __init__(self, max_items):
        self.max_items = max_items
        self.values = []

    def append(self, value):
        if len(self.values) < self.max_items:
            self.values.append(value)
            return value
        if value <= self.values[0]:
            return None
        self.values[0] = value
        self.values.sort()
        return value

    def sum(self):
        return sum(self.values)
