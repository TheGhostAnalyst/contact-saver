# Contacts Saver

A simple Python CLI tool to save and search contact information securely using Python’s built-in `shelve` module for persistent storage.

---

## Features

- Add multiple contacts with details like phone number, email, and birthday.
- Store multiple entries per contact owner.
- Search and display saved contacts.
- Persistent storage with easy-to-use CLI interface.

---

## Installation

1. Clone the repository:
```
   git clone https://github.com/TheGhostAnalyst/contacts-saver.git
   cd contacts-saver
   ```

2. (Optional) Create and activate a virtual environment:
```
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. Install dependencies:
```
   pip install pyinputplus
   ```

---

## Usage

Run the script:
```
python contacts_saver.py
```

You will see a menu with options:

1. Add a new contact
2. Look for a particular contact
3. Exit the program

Follow the prompts to add or search contacts.

---

## How It Works

* Contacts are saved in a persistent shelve database (`Contacts.db`).
* Each contact owner’s name is the key; multiple entries per owner are stored as a list.
* Each entry contains:

  * Phone number
  * Email (optional)
  * Birthday
  * Timestamp of when the contact was saved
* Searching by owner’s name retrieves all stored entries.

---

## Example Interaction
Welcome to The Ghost Analyst's Contacts Saver

Which of these operations would you like to perform:
1. Add a new contact
2. Look for a particular contact
3. Exit
=================

Enter the name of the owner: ghost
Enter the phone number: 1234567890
Enter the email (or * if not necessary): ghost@example.com
Enter the birthday (YYYY-MM-DD): 2000-01-01

Contact has been successfully saved to database.


---

## Dependencies

* Python 3.x
* [pyinputplus](https://pypi.org/project/PyInputPlus/) for robust user input handling.

Install pyinputplus with:
```
pip install pyinputplus
```

---

## License

MIT License © TheGhostAnalyst

---

## Contact

Feel free to reach out or collaborate via my GitHub profile:
[https://github.com/TheGhostAnalyst](https://github.com/TheGhostAnalyst)

---

*Build and manage your contacts efficiently and securely.*
