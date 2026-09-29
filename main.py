from validation import get_positive_integer, get_choice
from event import create_event, display_event
from reports import display_resource_report

from validation import get_positive_integer, get_choice

from event import create_event, display_event

from reports import display_resource_report


events = []


def create_new_event():
    print()
    print("***** CREATE NEW EVENT *****")

    event_name = input("Enter event name: ")

    print()
    print("Select event type:")
    print("1. Seminar")
    print("2. Workshop")
    print("3. Cultural Event")
    print("4. Sports Event")
    print("5. Conference")

    event_choice = get_choice(
        "Enter your choice (1-5): ",
        1,
        5
    )

    if event_choice == 1:
        event_type = "Seminar"

    elif event_choice == 2:
        event_type = "Workshop"

    elif event_choice == 3:
        event_type = "Cultural Event"

    elif event_choice == 4:
        event_type = "Sports Event"

    else:
        event_type = "Conference"

    attendees = get_positive_integer(
        "Enter expected number of attendees: "
    )

    venue_capacity = get_positive_integer(
        "Enter venue capacity: "
    )

    available_volunteers = get_positive_integer(
        "Enter available volunteers: "
    )

    event = create_event(
        event_name,
        event_type,
        attendees,
        venue_capacity,
        available_volunteers
    )

    events.append(event)

    display_event(event)

    display_resource_report(event)


def view_events():
    print()
    print("***** SAVED EVENTS *****")

    if len(events) == 0:
        print("No events have been created yet.")
        return

    for number, event in enumerate(events, start=1):
        print()
        print("Event", number)
        print("Name:", event["name"])
        print("Type:", event["type"])
        print("Attendees:", event["attendees"])
        print("Venue capacity:", event["capacity"])
        print("Available volunteers:", event["volunteers"])


def main_menu():

    while True:

        print()
        print("================================")
        print("      EVENT RESOURCE PLANNER")
        print("================================")
        print("1. Create New Event")
        print("2. View Saved Events")
        print("3. Exit")

        choice = get_choice(
            "Enter your choice (1-3): ",
            1,
            3
        )

        if choice == 1:
            create_new_event()

        elif choice == 2:
            view_events()

        elif choice == 3:
            print()
            print("Thank you for using Event Resource Planner.")
            print("Goodbye!")
            break


main_menu()