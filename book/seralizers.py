from rest_framework import serializers
from book.models import Book

class BookSeralizer(serializers.Serializer):
    title = serializers.CharField(max_length=300, required=True)
    author = serializers.CharField(max_length=100, required=True)
    isbn = serializers.CharField(required=True)
    publication_date = serializers.DateTimeField(required=True)
    genre = serializers.CharField(required=False)
    available_copies = serializers.IntegerField(required=True)

class BookModelSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'