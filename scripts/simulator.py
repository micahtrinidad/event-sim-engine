from events import Event
from state import State
from queue import EventQueue
from actions import ScheduleEventAction
from strategy import HeartBeatStrategy



def run(event_list: list, strategy=None) -> State:
    new_state = State()
    #sorted_events = sorted(event_list, key=lambda e: e.timestamp)
    queue = EventQueue()

    # Populate the queue with events from event list
    for event in event_list:
        queue.push(event)

    # Pop the events in the order that the priority queue put them in
    while not queue.is_empty():
        event = queue.pop()

        new_state.current_time = event.timestamp
        if event.type == "PRICE_UPDATE":
            new_state.price = event.price

        # If there is a strategy, do something
        if strategy is not None:
            actions = strategy.on_event(event, new_state)

            for action in actions:
                if isinstance(action, ScheduleEventAction):
                    queue.push(action.event)
                    print(f"  scheduled {action.event.type} at {action.event.timestamp}")
    
    return new_state

if __name__ == "__main__":
    event_list = [
    Event(timestamp=1.0, type="TICK"),
    Event(timestamp=1.0, type="PRICE_UPDATE", price=100.0),
    Event(timestamp=2.0, type="PRICE_UPDATE", price=99.5)
    ]

    strategy = HeartBeatStrategy(interval=1.0, end_time=5.0)
    final_state = run(event_list, strategy=strategy)
    print("Final state:", final_state.current_time, final_state.price)
