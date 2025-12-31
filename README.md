# event-sim-engine
event driven sim in python that processes time-ordered data events, updates system states, and evaluates strategy logic in a controlled, testable environment

The system's purpose:
- read time-ordered events (from CSV or generated)
- push them through an event queue
- update a shared state
- allow pluggable strategies to react to events
- log results and metrics

This project falls under these keywords:
- Backend system, modular, deterministic, testable

I will end up with:
- Event (represents something happening at a point in time)
- EventQueue (orders events by timestamp aka priorityqueue)
- state (holds current system state like price, positions, counters, etc.)
- strategy (defines how system reacts to events)
- simulator (the engine that pulls events -> updates states -> invokes strategy)

🔍 YouTube search terms (use these literally)

Search one at a time, skim, don’t binge.

Core concepts

event driven architecture explained

discrete event simulation python

simulation engine architecture

event loop architecture explained

priority queue event simulation

Systems thinking

backend system design event processing

how event queues work

deterministic simulation systems

Python-specific (optional)

python heapq priority queue

python dataclasses for architecture

You are learning patterns, not copying code.
