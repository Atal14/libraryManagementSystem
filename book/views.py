from book.seralizers import BookSeralizer, BookModelSeralizer
from rest_framework.views import APIView
from book.models import Book
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BookGetAllView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookModelSeralizer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookCreateView(APIView):
    def post(self, request, format=None):
        serializer_class = BookModelSeralizer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        new_book = serializer_class.validated_data;
        
        created_book = Book.objects.create(**new_book)

        return Response(BookModelSeralizer(created_book).data, status=status.HTTP_201_CREATED)

class BookUpdateView(APIView):
    def put(self, request, id):
        try:
            book = Book.objects.get(id=id)
            serializer = BookModelSeralizer(book, data=request.data)
            if serializer.is_valid():
                book.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)


class BookDeleteView(APIView):
    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return Response({"message": "Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)