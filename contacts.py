import subprocess


def get_contact(name):

    name = (
        name
        .lstrip("@")
        .replace("_", " ")
    )

    script = f'''
    tell application "Contacts"

        try

            set targetPerson to first person whose name contains "{name}"

            return value of first phone of targetPerson

        on error

            return "__NOT_FOUND__"

        end try

    end tell
    '''

    result = subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )

    output = result.stdout.strip()

    if output == "__NOT_FOUND__":
        return None

    return output
