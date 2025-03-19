from django.db import models
from book.models import Book
from member.models import Member

# Create your models here.
class Borrowing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
    
    class Meta:
        db_table = 'borrow'