from rest_framework import serializers
from .models import Note

class NoteSerialilzer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Note
        fields = '__all__'