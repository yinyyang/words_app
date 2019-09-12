from django.db import models

# Create your models here.
from django.db.models import F
class Listen(models.Model):
    youdao = models.TextField()
    english= models.TextField()
    book_num=models.IntegerField()
    book_t=models.TextField()

    class Meta:
        ordering = [F('book_num').asc(),F('book_t').asc()]
    def __str__(self):
        return  "%s |  %s" % (
            self.english,
            self.youdao,
        )
