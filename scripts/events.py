class Event:
    def __init__(self, timestamp, type, price=None, data=None):
        self.timestamp = timestamp
        self.type = type
        self.price = price
        self.data = data