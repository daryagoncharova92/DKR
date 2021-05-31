from .models import Note

class DataBase:
    def __init__(self):
        self.notes = Note.objects.all()

    def all(self):
        return self.notes.all()

    def get_by_id(self, id):
        return self.notes.objects.get(pk=id)

    def update(self, data):
        note = Note(**data)
        note.pk = data['id']
        note.save()
        return True

    def delete(self, id):
        self.notes.get(pk=id).delete()
        return True

    def create(self, data):
        Note(**data).save()
        return True