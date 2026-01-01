from events import Event
from state import State

event_list = [
    Event(timestamp=1.0, type="PRICE_UPDATE", price=100.0),
    Event(timestamp=1.5, type="PRICE_UPDATE", price=99.5),
    Event(timestamp=2.5, type="PRICE_UPDATE", price=104.0)
]

def run(event_list: list) -> State:
    new_state = State()
    sorted_events = sorted(event_list, key=lambda e: e.timestamp)

    for event in sorted_events:
        # Advance through the sim
        new_state.current_time = event.timestamp
        if event.type == "PRICE_UPDATE":
            new_state.price = event.price
    
    print(
        f"time={new_state.current_time:.1f}, "
        f"event={event.type}, "
        f"price={new_state.price}"
    )
    
    return new_state

if __name__ == "__main__":
    final_state = run(event_list)
    print("Final state:", final_state.current_time, final_state.price)
