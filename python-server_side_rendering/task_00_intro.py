#!/usr/bin/python3
"""
This contains a function:
generate_invitations
"""


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print('The template must be a string')
        return
    if not template:
        print('Template is empty, no output files generated.')
        return
    if not isinstance(attendees, list) and \
            not all(isinstance(a, dict) for a in attendees):
        print('The attendees must be a list of dictionary')
        return
    if not attendees:
        print('No data provided, no output files generated.')
        return

    for i, attendee in enumerate(attendees, start=1):
        data = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A")
        }
        invitation = template.format(**data)

        filename = f"output_{i}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(invitation)
