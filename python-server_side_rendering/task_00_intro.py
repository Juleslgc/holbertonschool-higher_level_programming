#!/usr/bin/python3
"""
This contains a function:
generate_invitations
"""


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        raise TypeError('The template must be a string')
    if not template:
        raise TypeError('Template is empty, no output files generated.')
    if not isinstance(attendees, list) and \
            not all(isinstance(a, dict) for a in attendees):
        raise TypeError('The attendees must be a list of dictionary')
    if not attendees:
        raise TypeError('No data provided, no output files generated.')

    for i, attendee in enumerate(attendees, start=1):
        data = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A")
        }
        invitation = template.format(**data)

        filename = "output_{i}.txt"
        with open(filename, "w") as file:
            file.write(invitation)
