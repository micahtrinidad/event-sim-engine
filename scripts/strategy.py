from actions import ScheduleEventAction
from events import Event

# Parent class
# Default is to do nothing
class Strategy:
    def on_event(self, event, state) -> list:
        return []
    
class HeartBeatStrategy(Strategy):
    def __init__(self, interval=1.0, end_time=5.0):
        self.interval = interval
        self.end_time = end_time

    def on_event(self, event, state):
        """
        Schedule a TICK at (current_time + interval) until end_time.
        """
        if event.type != "TICK":
            return []
        
        next_time = state.current_time + self.interval

        if next_time <= self.end_time:
            tick_event = Event(timestamp=next_time, type="TICK", price=None)
            return [ScheduleEventAction(tick_event)]

        return []
