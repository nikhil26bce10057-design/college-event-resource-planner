from calculation import (
    calculate_chairs,
    calculate_volunteers,
    calculate_registration_desks,
    calculate_water_bottles
)

from analysis import (
    check_venue,
    check_resource,
    get_event_summary,
    get_volunteer_gap
)


def display_resource_report(event):
    print()
    print("===== RESOURCE PLAN =====")

    attendees = event["attendees"]

    chairs = calculate_chairs(attendees)
    required_volunteers = calculate_volunteers(attendees)
    registration_desks = calculate_registration_desks(attendees)
    water_bottles = calculate_water_bottles(attendees)

    print("Chairs required:", chairs)
    print("Volunteers required:", required_volunteers)
    print("Registration desks:", registration_desks)
    print("Water bottles:", water_bottles)

    print()
    print("===== RESOURCE ANALYSIS =====")

    venue_status = check_venue(
        attendees,
        event["capacity"]
    )

    volunteer_status = check_resource(
        required_volunteers,
        event["volunteers"]
    )

    volunteer_gap = get_volunteer_gap(
        required_volunteers,
        event["volunteers"]
    )

    print("Venue status:", venue_status)
    print("Volunteer status:", volunteer_status)

    if volunteer_gap > 0:
        print("Additional volunteers needed:", volunteer_gap)
    else:
        print("Additional volunteers needed: 0")

    print()
    print("===== EVENT SUMMARY =====")
    print(
        get_event_summary(
            attendees,
            event["capacity"]
        )
    )