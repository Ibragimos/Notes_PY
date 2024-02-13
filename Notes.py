import os
import pickle
from datetime import datetime

class Note:
    def __init__(self, title, content, date=None):
        self.title = title
        self.content = content
        self.date = date if date else datetime.now()

    def __str__(self):
        return f"{self.title} - {self.content} - {self.date}"

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        new_note = Note(title, content)
        self.notes.append(new_note)

    def save_notes(self):
        file_path = "T/notes.pickle"
        with open(file_path, "wb") as file:
            pickle.dump(self.notes, file)
        print("Notes saved successfully.")

    def load_notes(self):
        file_path = "T/notes.pickle"
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                self.notes = pickle.load(file)
        print("Notes loaded successfully.")

    def list_notes(self):
        if self.notes:
            for index, note in enumerate(self.notes):
                print(f"{index + 1}. {note}")
        else:
            print("No notes available.")

    def edit_note(self, index, title, content):
        self.notes[index - 1].title = title
        self.notes[index - 1].content = content
        self.notes[index - 1].date = datetime.now()
        print("Note edited successfully.")

    def delete_note(self, index):
        del self.notes[index - 1]
        print("Note deleted successfully.")

    def filter_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.date.date() == date.date()]
        return filtered_notes

def main_function():
    note_manager = NoteManager()

    while True:
        print("\n1. Create a new note")
        print("2. Show all notes")
        print("3. Filter notes by date")
        print("4. Edit a note")
        print("5. Delete a note")
        print("6. Save notes")
        print("7. Load notes")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note_manager.create_note(title, content)
        elif choice == "2":
            note_manager.list_notes()
        elif choice == "3":
            date_str = input("Enter the date in format YYYY-MM-DD: ")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            filtered_notes = note_manager.filter_notes_by_date(date)
            print("Filtered Notes:")
            for note in filtered_notes:
                print(note)
        elif choice == "4":
            index = int(input("Enter the index of the note you want to edit: "))
            title = input("Enter the new title: ")
            content = input("Enter the new content: ")
            note_manager.edit_note(index, title, content)
        elif choice == "5":
            index = int(input("Enter the index of the note you want to delete: "))
            note_manager.delete_note(index)
        elif choice == "6":
            note_manager.save_notes()
        elif choice == "7":
            note_manager.load_notes()
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_function()