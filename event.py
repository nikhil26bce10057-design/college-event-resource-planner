def create_event(name, event_type, attendees, capacity, volunteers):
    event = {
        "name": name,
        "type": event_type,
        "attendees": attendees,
        "capacity": capacity,
        "volunteers": volunteers
    }

    return event


def display_event(event):
    print()
    print("===== EVENT DETAILS =====")
    print("Event:", event["name"])
    print("Event type:", event["type"])
    print("Expected attendees:", event["attendees"])
    print("Venue capacity:", event["capacity"])
    print("Available volunteers:", event["volunteers"])