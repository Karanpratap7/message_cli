import subprocess
import sys
from contacts import get_contact


def send_message(contact, text):

    number = get_contact(contact)

    if number is None:
        print("Contact not found")
        return

    print(f"Sending to {contact}")

    number = (
        number
        .replace(" ", "")
        .replace("-", "")
    )

    script = f'''
    tell application "Messages"
        set targetService to first service whose service type = iMessage
        set targetBuddy to buddy "{number}" of targetService
        send "{text}" to targetBuddy
    end tell
    '''

    subprocess.run(
        ["osascript", "-e", script]
    )

    print("✓ Sent")

if __name__ == "__main__":

    person = (
        sys.argv[1]
        .lstrip("@")
        .replace("_", " ")
    )
    message = sys.argv[2]

    send_message(person, message)