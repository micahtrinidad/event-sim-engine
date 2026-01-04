from events import Event
from state import State
from queue import EventQueue

event_list = [
    Event(timestamp=1.0, type="PRICE_UPDATE", price=100.0),
    Event(timestamp=1.5, type="PRICE_UPDATE", price=99.5),
    Event(timestamp=2.5, type="PRICE_UPDATE", price=104.0)
]

def run(event_list: list) -> State:
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

            print(f"time={new_state.current_time:.1f}, event={event.type}, price={new_state.price}")
    
    return new_state

if __name__ == "__main__":
    final_state = run(event_list)
    print("Final state:", final_state.current_time, final_state.price)
