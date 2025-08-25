import shelve
from datetime import datetime
import pyinputplus as pyip
import time
import sys

DB_NAME = 'contacts.db'

def add_contact(name, number, email, birthday):
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    contact_entry = {
        'Number': number,
        'Email': email,
        'Birthday': birthday,
        'Date saved': now
    }

    with shelve.open(DB_NAME, writeback=True) as db:
        if name in db:
            db[name].append(contact_entry)
        else:
            db[name] = [contact_entry]


def search_contact(name):
    with shelve.open(DB_NAME) as db:
        if name in db:
            print(f'\nContact entries for "{name}":\n' + '-' * 40)
            for i, entry in enumerate(db[name], start=1):
                print(f'# Entry {i}')
                print(f"Number     : {entry.get('Number', 'N/A')}")
                print(f"Birthday   : {entry.get('Birthday', 'N/A')}")
                print(f"Email      : {entry.get('Email', 'Skipped')}")
                print(f"Date saved : {entry.get('Date saved', 'N/A')}")
                print('-' * 40)
        else:
            print(f'No entries found for "{name}".')


def show_all_contacts():
    with shelve.open(DB_NAME) as db:
        if not db:
            print("\nNo contacts saved yet.")
            return
        print("\nAll saved contacts:\n" + "-" * 30)
        for name in db:
            print(f"- {name}")
        print("-" * 30)


# Main application loop
while True:
    try:
        print("\nWelcome to The Ghost Analyst's Contact Saver")
        choice = pyip.inputInt("""\nChoose an operation:
1. Add a new contact
2. Search for a contact
3. View all saved contacts
4. Exit
================= """, min=1, max=4)

        if choice == 1:
            print('\nPreparing to save a new contact...')
            time.sleep(1)

            name = input("Enter the contact owner's name: ").strip().lower()
            number = pyip.inputNum("Enter the contact number (digits only): ", min=1000000)

            email = input("Enter the email (optional, press Enter to skip): ").strip()
            if not email:
                email = "Skipped"

            while True:
                birthday = input("Enter the birthday (YYYY-MM-DD): ").strip()
                try:
                    datetime.strptime(birthday, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid format. Please use YYYY-MM-DD.")

            add_contact(name, number, email, birthday)
            print('\nContact saved successfully.\n')

        elif choice == 2:
            name = input("Enter the name to search for: ").strip().lower()
            print('Searching...')
            time.sleep(1)
            search_contact(name)

        elif choice == 3:
            show_all_contacts()

        elif choice == 4:
            print('\nThank you for using The Ghost Analyst\'s Contact Saver. Goodbye.\n')
            break

    except KeyboardInterrupt:
        print('\nKeyboardInterrupt detected. Exiting gracefully...')
        time.sleep(1)
        sys.exit()
