import sys

from notebook import Notebook, Note

class Menu(object):
    """Display a menu and respond to choices when run.."""
    def __init__(self):
        # super(Menu, self).__init__()
        # self.arg = arg
            self.notebook = Notebook()
            self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
            }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        """Displays the Menu and respond to choices"""
        while True:
            self.display_menu()
            choices = input("Enter an option: ")
            action = self.choices.get(choices)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self, notes=None):
        """finds notes"""
        if not notes:
            notes = self.notebook.notes
            for note in notes:
                print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
        

    def add_note(self):
        memo = input("Enter a Memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id = input("Enter id: ")
        memo = input("Enter memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)

        if tags:
            self.notebook.modify_tag(id, tags)

    def quit(self):
        print("Thank you for using your Notebook today")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
