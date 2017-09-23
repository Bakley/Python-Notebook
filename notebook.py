import datetime # built in

# stores the next callable id
last_id = 0



class Note(object): # this is for py 2
    """Notes are shorts memo stored in a Notebook.
    Each note should have a unique id, tags and stores the day created."""

    def __init__(self, memo, tags=""):
        # super(Note, self).__init__()
        # self.arg = arg
        '''initialize a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter text.
        Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and tags.'''

        return filter in self.memo or filter in self.tags


class Notebook(object):
    """docstring for Notebook."""
    def __init__(self):
        # super(Notebook, self).__init__()
        # self.arg = arg
        ''' initialize a notebook with empty list'''
        self.notes = []

    def new_note(self, memo, tags=''):
        """Create a new note and add it to the Notebook"""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tag(self, note_id, tags):
        """Find the note with the given id and change its tag to the condition
        given value"""
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [note for note in self.notes if note.match(filter)]
