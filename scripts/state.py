# State starts empty
# Simulator mutates it
class State:
    def __init__(self):
        self.current_time = 0.0
        self.price = None
        self.price_history = []
