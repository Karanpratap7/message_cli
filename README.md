# Message CLI

Send iMessages directly from your terminal using your macOS Contacts.
# "Made this just cause switching windows was breaking my flow and I got annoyed and the tinkering spirit in me wanted a solution."

Example:

```bash
message "@John Doe" "Hello from terminal"
```

This project:

* Reads contacts from the macOS Contacts app
* Resolves contact names to phone numbers
* Sends messages through iMessage
* Supports spaces in contact names

---

## Requirements

* macOS
* Python 3
* iMessage configured and working
* Contacts synced locally

Check Python:

```bash
python --version
```

---

## Project Structure

```text
message-cli/
│
├── send.py
├── contacts.py
└── message
```

---

## Installation

Clone:

```bash
git clone <repo-url>
cd message-cli
```

No external packages required.

---

## Setup

### 1. Make terminal command executable

```bash
chmod +x message
```

Move command into PATH:

```bash
sudo mv message /usr/local/bin/
```

### 2. Configure script path

Edit:

```bash
nano /usr/local/bin/message
```

Example:

```zsh
#!/bin/zsh
python /Users/YOUR_USERNAME/message-cli/send.py "$@"
```

Save:

```text
Ctrl + O
Enter
Ctrl + X
```

---

## Usage

Send message:

```bash
message "@Mom" "Reached safely"
```

Contact with spaces:

```bash
message "@Roommate" "Send notes"
```

---

## How It Works

1. User runs terminal command
2. Python extracts contact name
3. AppleScript queries Contacts
4. Phone number is returned
5. Messages app sends iMessage

Flow:

```text
Terminal
   ↓
Python
   ↓
Contacts (AppleScript)
   ↓
Messages
   ↓
Recipient
```

---

## Troubleshooting

### Contact not found

Check exact contact name:

```bash
python send.py "@Contact"
```

### Sends SMS instead of iMessage

Open Messages and verify:

```text
Settings
→ iMessage
→ Enabled
```

Confirm recipient supports iMessage.

### Permission issues

Grant access:

```text
System Settings
→ Privacy & Security
→ Automation
```

Allow:

* Terminal → Contacts
* Terminal → Messages

---

## Future Improvements

* Fuzzy search
* Group messaging
* Send attachments
* Contact autocomplete
* Message history
* Voice commands
* Scheduled messages

---

Built with Python + AppleScript + excessive confidence in terminal workflows.
