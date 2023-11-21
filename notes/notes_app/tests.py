from django.test import TestCase
from .models import Note
from .serializers import NoteSerializer


class NoteSerializerTestCase(TestCase):
    def test_note_serializer(self):
        note_data = {
            'title': 'Test Note',
            'content': 'This is a test note.',
        }
        note = Note.objects.create(**note_data)
        serializer = NoteSerializer(instance=note)
        self.assertEqual(serializer.data['id'], note.id)
        self.assertEqual(serializer.data['title'], note.title)
        self.assertEqual(serializer.data['content'], note.content)

