def check_venue(attendees, capacity):
    if attendees > capacity:
        return "Insufficient"
    else:
        return "Suitable"


def check_volunteers(attendees, volunteers):
    recommended = (attendees + 49) // 50

    if volunteers >= recommended:
        return "Adequate"
    else:
        return "Insufficient"


def get_event_summary(attendees, capacity):
    if attendees > capacity:
        return "The expected attendance exceeds the venue capacity."

    elif attendees == capacity:
        return "The venue will be at full capacity."

    else:
        remaining = capacity - attendees
        return f"The venue has space for {remaining} more people."


def check_resource(required, available):
    if available >= required:
        return "Adequate"
    else:
        return "Insufficient"


def get_volunteer_gap(required, available):
    if available >= required:
        return 0

    return required - available